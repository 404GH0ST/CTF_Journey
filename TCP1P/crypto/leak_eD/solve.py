n = 14860853369944304576220993465945783364682381383560084173901940941019909637106553872879402687512699589355294361128757426007505024461141510744378371405675362861067114724585888664156433200597487760931661583876608151510126088338988327910829014466849572649500268022015782359782713044157988606913179077356862544281593283001257460416421853615051099159635352316012078155141240508343707445133522570188768949366285923210156951827471185692438273511684719748649524936945330497890284672615338236726828506542364507700538346815467435767523373084197795849328086495053047422054752577219614826038347807669030442951647428430384459092367
e = 5
c = 6014205168199442540426903567863221018736762068998015501367915649754291514036525288108812934262774778629288137476569283744297844738593424993542031460550821955772582633197445381135925175729325446251201554850639269289384605544741241895438945468244041912060528804024807945050899341007120381623323838327896979680113671102774422929130794893635773984498901075576287980009235428436651506116605277355748765443382522338458636557199535530239360251468635843191703118623028913816979213129206522865098604483436064582877270010680247349629636994479793039646163088349494170148984939870188800876562981379562879086946860896587060166440
dp = 63130804865387686409720734748064136565646144877560835650036907186045506940345078038548402787572800091452332957412308644456890057020789224810204226351603649879869278194266101261706328655548577160044475061236324119753673889059114249399219507191936672257551882670536737128706462087062179928589812154606105209727
p = None
for kp in range(1,e):
    x = (e*dp-1)/kp+1
    if (x in ZZ):
        if (n/x) in ZZ:
            p = x
            break
    if p is not None:
        break

q = n/p
phi = (p-1) * (q-1)
d = inverse_mod(e, phi)
m = pow(c,d,n)
print(bytes.fromhex(hex(m)[2:]).decode())