# -*- coding: utf-8 *-*
import sys
from Naked.toolshed.shell import muterun_rb


asciidoctor = './gemEnv/gems/asciidoctor-1.5.5/bin/asciidoctor'
asciidoctor_pdf = './gemEnv/gems/asciidoctor-pdf-1.5.0.alpha.15/bin/asciidoctor-pdf'




def adocToPDF(file):
    return muterun_rb(asciidoctor_pdf, file)

def adocToHTML(file):
    return muterun_rb(asciidoctor, file)


if __name__ == '__main__':
    file = 'basic-example.adoc'
    response = adocToPDF(file)
    if response:
        print("Worked!!")
    else:
        print("Nope!!")
