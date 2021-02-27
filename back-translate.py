import pandas as pd
import torch
import sys
from prog import printProgressBar

def back_translate(en_claim, en2de, de2en):
    de_claim = en2de.translate(en_claim)
    bt_claim = de2en.translate(de_claim)

if __name__ == "__main__": 
    og_claims = pd.read_json('claims_train.jsonl', lines=True)['claim'] # loading the already saved de back translated claims for comparison
    df = pd.read_json(sys.argv[1], lines=True) # loading the claims to back translate
    english_claims = df['claim']
    n = len(english_claims)

    back_translated_claims = [None] * n
    
    en2ru = torch.hub.load('pytorch/fairseq', 'transformer.wmt19.en-ru.single_model', tokenizer='moses', bpe='fastbpe')
    ru2en = torch.hub.load('pytorch/fairseq', 'transformer.wmt19.ru-en.single_model', tokenizer='moses', bpe='fastbpe')
    #en2de = torch.hub.load('pytorch/fairseq', 'transformer.wmt19.en-de', checkpoint_file='model1.pt:model2.pt:model3.pt:model4.pt', tokenizer='moses', bpe='fastbpe')
    #de2en = torch.hub.load('pytorch/fairseq', 'transformer.wmt19.de-en', checkpoint_file='model1.pt:model2.pt:model3.pt:model4.pt', tokenizer='moses', bpe='fastbpe')
    #en2de.cuda() # for faster translation once i have an NVIDIA GPU and driver
    #de2en.cuda()

    # disables dropout
    en2ru.eval()
    ru2en.eval()

    #printProgressBar(0, n, prefix='Progress:', suffix='translated claim 0 / %d' % (n), length=25)
    for i, en_claim in enumerate(english_claims):
        print("%d / %d" % (i+1, n))
        print("Original claim: ", og_claims[i])
        print("GER B-T claim:  ", en_claim)
        ru_claim = en2ru.translate(en_claim)
        bt_claim = ru2en.translate(ru_claim)
        back_translated_claims[i] = bt_claim
        print("2RU B-T claim:  ", bt_claim)
        #printProgressBar(i+1, n, prefix='Progress:', suffix='translated claim %d / %d' % (i+1, n), length=25)

    df['claim'] = back_translated_claims

    df.to_json(path_or_buf="double_bt_de2ru_claims_train.jsonl", orient="records", lines=True)
