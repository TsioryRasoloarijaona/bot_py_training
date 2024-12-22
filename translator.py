from googletrans import Translator 

def translate (sentence ) :
    translator = Translator() ;
    translated = translator.translate( sentence, src='auto' , dest="fr")
    print(translated) ;


