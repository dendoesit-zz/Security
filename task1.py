
#brute force attack Cipher
sentence = 'HUKHZMVYCH SVYAO HAJHU UVAIL JVTWB ALKIF ZAHAB YLOLOHZWHZ ZLKAO YVBNO TVYLI HAASL ZHUKW LYPSZ AOHUF VBOHCLPUNV SKAOV BNOFV BILAD PJLOP ZOLPN OAHUK OLJVT LZUVD MYVTAOLZAV YTPUN VMPZL UNHYK VMDOP JODLI LHYAP KPUNZ HUKNYLHADL HYPUL ZZPZV UOPTV YPDVB SKDHR LOPTO PZUHT LPZWL YLNYPUMYVT SVYKV MAOLY PUNZI VVRMP CLJOH WALYV UL'
sentence = sentence.replace(' ','')


shift=0
while(shift<26):
    result =" "
    for i in sentence.lower():

        if ('a'<=i<='z'):
            newChr= chr(((ord(i)-ord('a')+ shift) %26)+ord('a'))
            result += newChr
        else:
            print('only letters from a to z are allowed')
            break
    shift +=1
    print(shift,result)



result = 'andasforvalorthatcannotbecomputedbystaturehehaspassedthroughmorebattlesandperilsthanyouhaveingoldthoughyoubetwicehisheightandhecomesnowfromthestormingofisengardofwhichwebeartidingsandgreatwearinessisonhimoriwouldwakehimhisnameisperegrinfromlordoftheringsbookfivechapterone'