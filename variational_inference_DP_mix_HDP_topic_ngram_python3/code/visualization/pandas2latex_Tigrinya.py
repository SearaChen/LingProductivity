# coding: utf-8

import pandas as pd
import pandas2latex as p2l
import pytablewriter, sys

ipa2latex = {
	"ä":r"{\textturna}",
	"ə":r"{\textbari}",
	"ḥ":r"{\textcrh}",
	"ś":r"\'{s}",
	"š":r"{\textesh}",
	"ḳ":r"k'",
	"ḳʰ":r"k'\textsuperscript{h}",
	"č":r"{\textteshlig}",
	"ḫ":r"\textsubwedge{h}",
	"y":r"j",
	"ñ":r"{\textltailn}",
	"ʾ":r"{\textglotstop}",
	"ʿ":r"{\textrevglotstop}",
	"ž":r"{\textyogh}",
	"ǧ":r"{\textdyoghlig}",
	"ṭ":r"t'",
	"č̣":r"{\textteshlig}'",
	"p̣":r"p'",
	"ṣ":r"s'",
	"ṣ́":r"\'{s}'",
	"g":r"{\textscriptg}"
}

def convert_context(context):
	if context.startswith('__'):
		context = context.replace('__', '_,')
	elif context.endswith('__'):
		context = context.replace('__', ',_')
	else:
		context = context.replace('_', ',')
	
	return ','.join([ipa2latex_func(ipa) for ipa in context.split(',')])
	# return context

def ipa2latex_func(ipa):
	if ipa in ipa2latex:
		return ipa2latex[ipa]
	elif ipa.endswith('w') and len(ipa) > 1:
		return ipa2latex_func(ipa.split('w')[0]) + r"{\textsuperscript{w}}"
	else:
		return ipa

if __name__ == '__main__':
	pd.set_option('display.max_colwidth', -1)

	path = sys.argv[1]
	df = pd.read_csv(path, encoding='utf-8')

	# For ngram rep/
	sublex_id = int(path.split('sublex-')[1][0]) # int(sys.argv[2])
	df.loc[:,'context'] = df.decoded_context.map(convert_context)
	df.loc[:,'value'] = df.decoded_value.map(ipa2latex_func)
	representativeness_latex = r'$R(x_{\textrm{new}}, \mathbf{u},' + ' {sublex})$'.format(sublex=sublex_id)
	df.loc[:,representativeness_latex] = df.representativeness
	df.loc[:,'freq.'] = df.frequency
	df = df[['context', 'value', representativeness_latex, 'freq.']]

	# For probable words
	# sublex_id = int(path.split('sublex-')[1][0]) # int(sys.argv[2])
	# sublexes = ['sublex_%i' % k for k in range(6) if k!=sublex_id]
	# df = df.rename(columns={'sublex_%i' % sublex_id:'prob'})
	# df['prob'] = df.prob.map(lambda value: '%0.6f' % value)
	# df.loc[:,'IPA'] = df.IPA_vsv.map(lambda string: ''.join([ipa2latex_func(code) for code in string.split('|')]))

	# df = df[['IPA','prob']]

	# print df.family.value_counts()

	latex_table = df.to_latex(encoding='utf-8', index=False, escape = False, longtable = False)
	# latex_table = latex_table.replace(r'\textbackslash','\\').replace('\{','{').replace('\}','}')
	# p2l.print_utf8(latex_table)
	with open(sys.argv[2], 'w') as f:
		f.write(latex_table)