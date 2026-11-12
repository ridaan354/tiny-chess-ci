import json,os,random,sys,urllib.request as U,urllib.error as E
V=os.environ["MAKEFUN_ENV_URL"]
ND=150000
MT=100000
VL=[0,100,320,330,500,900,20000]
PS=["KKKKKKKKLMMGGMMLLJIKKIJLKKKOOKKKLLMPPMLLMMOQQOMMUUUUUUUUKKKKKKKK","ACEEEECACGKLLKGCELMNNMLEEKNOONKEELNOONLEEKMNNMKECGKKKKGCACEEEECA","GIIIIIIGILKKKKLIIMMMMMMIIKMMMMKIILLMMLLIIKLMMLKIIKKKKKKIGIIIIIIG","KKKLLKKKJKKKKKKJJKKKKKKJJKKKKKKJJKKKKKKJJKKKKKKJLMMMMMMLKKKKKKKK","GIIJJIIGIKLKKKKIILLLLLKIKKLLLLKJJKLLLLKJIKLLLLKIIKKKKKKIGIIJJIIG","OQMKKMQOOOKKKKOOIGGGGGGIGEECCEEGECCAACCEECCAACCEECCAACCEECCAACCE"]
TB=[[(ord(c)-75)*5 for c in s] for s in PS]
KN=(-33,-31,-18,-14,14,18,31,33)
KG=(-17,-16,-15,-1,1,15,16,17)
DG=(-17,-15,15,17)
RT=(-16,-1,1,16)
R=random.Random(1)
ZP=[[R.getrandbits(64) for _ in range(128)] for _ in range(13)]
ZS=R.getrandbits(64)
ZC=[R.getrandbits(64) for _ in range(16)]
ZE=[R.getrandbits(64) for _ in range(8)]
S64=[s for s in range(128)if not s&136]
CM=[15]*128
for s,m in ((0,13),(7,14),(4,12),(112,7),(119,11),(116,3)):CM[s]=m
nd=0;tt={};kl=[0]*128;hs={};b=[0]*128;sd=1;cs=0;ep=-1;kp=[4,116];hh=0;st=[];hg={}
class A(Exception):pass
def nm(s):return chr(s%8+97)+str((s>>4)+1)
def uc(m):
 p=(m>>14)&7
 return nm(m&127)+nm(m>>7&127)+("nbrq"[p-2] if p else "")
def pu(u):
 f=ord(u[0])-97+(int(u[1])-1)*16
 t=ord(u[2])-97+(int(u[3])-1)*16
 p="nbrq".index(u[4])+2 if len(u)>4 else 0
 return f|t<<7|p<<14
def at(s,by):
 for d in DG:
  t=s+d
  while not t&136:
   p=b[t]
   if p:
    if p==by*3 or p==by*5:return 1
    break
   t+=d
 for d in RT:
  t=s+d
  while not t&136:
   p=b[t]
   if p:
    if p==by*4 or p==by*5:return 1
    break
   t+=d
 for d in KN:
  t=s+d
  if not t&136 and b[t]==by*2:return 1
 for d in KG:
  t=s+d
  if not t&136 and b[t]==by*6:return 1
 for d in (-15,-17) if by>0 else (15,17):
  t=s+d
  if not t&136 and b[t]==by:return 1
 return 0
def gn(cp=False):
 global b
 ms=[]
 for f in S64:
  p=b[f]
  if not p or (p>0)!=(sd>0):continue
  a=abs(p)
  if a==1:
   d=16 if p>0 else -16
   t=f+d
   if not b[t]:
    pr=t>=112 if p>0 else t<16
    if pr:
     for q in (5,4,3,2):ms.append(f|t<<7|q<<14)
    elif not cp:
     ms.append(f|t<<7)
     if (f>>4)==(1 if p>0 else 6):
      t2=f+d*2
      if not b[t2]:ms.append(f|t2<<7)
   for d2 in (d-1,d+1):
    t=f+d2
    if t&136:continue
    q=b[t]
    if q and (q>0)!=(p>0) or t==ep:
     pr=t>=112 if p>0 else t<16
     if pr:
      for r in (5,4,3,2):ms.append(f|t<<7|r<<14)
     else:ms.append(f|t<<7)
  elif a==2 or a==6:
   for d in KN if a==2 else KG:
    t=f+d
    if t&136:continue
    q=b[t]
    if not q or (q>0)!=(p>0):
     if not cp or q:ms.append(f|t<<7)
  else:
   for d in DG if a==3 else RT if a==4 else DG+RT:
    t=f+d
    while not t&136:
     q=b[t]
     if not q:
      if not cp:ms.append(f|t<<7)
     else:
      if (q>0)!=(p>0):ms.append(f|t<<7)
      break
     t+=d
 if not cp and cs:
  k=kp[0] if sd>0 else kp[1];r=1 if sd>0 else 4
  if cs&r and not b[k+1] and not b[k+2] and b[k+3]==sd*4 and not at(k,-sd) and not at(k+1,-sd) and not at(k+2,-sd):ms.append(k|(k+2)<<7)
  if cs&r*2 and not b[k-1] and not b[k-2] and not b[k-3] and b[k-4]==sd*4 and not at(k,-sd) and not at(k-1,-sd) and not at(k-2,-sd):ms.append(k|(k-2)<<7)
 return ms
def mk(m):
 global cs,ep,sd,hh
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;p=b[f];cap=b[t];cc=16 if sd>0 else -16
 oc,oe,oh=cs,ep,hh
 st.append((m,cap,cs,ep,hh))
 hh^=ZP[p+6][f]
 b[f]=0
 if t==ep and abs(p)==1:
  cap=b[t-cc];b[t-cc]=0;hh^=ZP[cap+6][t-cc]
 elif cap:hh^=ZP[cap+6][t]
 nq=pr*sd if pr else p
 b[t]=nq;hh^=ZP[nq+6][t]
 if abs(p)==6:
  kp[0 if sd>0 else 1]=t
  if t==f+2:b[f+1]=b[f+3];b[f+3]=0;hh^=ZP[sd*4+6][f+3]^ZP[sd*4+6][f+1]
  elif t==f-2:b[f-1]=b[f-4];b[f-4]=0;hh^=ZP[sd*4+6][f-4]^ZP[sd*4+6][f-1]
 cs&=CM[f]&CM[t]
 ep=f+16 if abs(p)==1 and t==f+32 else f-16 if abs(p)==1 and t==f-32 else -1
 hh^=ZC[oc]^ZC[cs]
 if oe>=0:hh^=ZE[oe&7]
 if ep>=0:hh^=ZE[ep&7]
 hh^=ZS;sd=-sd
 return cap
def um():
 global cs,ep,sd,hh
 m,cap,cs,ep,hh=st.pop()
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;p=b[t]
 b[t]=cap
 b[f]=(1 if p>0 else -1) if pr else p
 if abs(b[f])==1 and t==ep and not cap:b[t-(16 if sd<0 else -16)]=sd
 if abs(b[f])==6:
  kp[0 if sd<0 else 1]=f
  if t==f+2:b[f+3]=b[f+1];b[f+1]=0
  elif t==f-2:b[f-4]=b[f-1];b[f-1]=0
 sd=-sd
def ev():
 s=0;nw=0;nb=0;wq=0;bq=0
 for i in S64:
  p=b[i]
  if p:
   a=abs(p)
   if a==3:
    if p>0:nw+=1
    else:nb+=1
   if a==5:
    if p>0:wq=1
    else:bq=1
   j=i if p>0 else i^112
   s+=(VL[a]+TB[a-1][j>>4<<3|j&7])*(1 if p>0 else -1)
 s+=30*(nw==2)-30*(nb==2)
 if not wq and not bq:
  for k,sg in ((kp[0],1),(kp[1],-1)):
   s+=sg*(14-(abs((k&7)*2-7)+abs((k>>4)*2-7)))*4
 return s if sd>0 else -s
def od(ms,tm,pl):
 def sc(m):
  if m==tm:return 1000000
  q=b[(m>>7)&127]
  if q:return 10000+VL[abs(q)]*10-VL[abs(b[m&127])]
  if m==kl[pl*2] or m==kl[pl*2+1]:return 5000
  return hs.get(m,0)
 ms.sort(key=sc,reverse=True)
 return ms
def qs(a,be,pl):
 global nd
 nd+=1
 if nd>ND:raise A
 if hg.get(hh,0)>1:return 0
 sp=ev()
 if sp>=be:return be
 if sp>a:a=sp
 if pl>40:return a
 ck=at(kp[0] if sd>0 else kp[1],-sd)
 ms=gn(not ck)
 od(ms,0,pl)
 lg=0
 for m in ms:
  if not ck:
   q=b[(m>>7)&127]
   if q and not (m>>14)&7 and sp+VL[abs(q)]+200<a:continue
  cp=mk(m)
  if at(kp[0] if sd<0 else kp[1],sd):um();continue
  lg=1
  try:s=-qs(-be,-a,pl+1)
  finally:um()
  if s>=be:return be
  if s>a:a=s
 return -MT+pl if ck and not lg else a
def sc(d,a,be,pl):
 global nd,sd,ep,hh
 nd+=1
 if nd>ND:raise A
 if hg.get(hh,0)>1:return 0
 if pl>60:return ev()
 ck=at(kp[0] if sd>0 else kp[1],-sd)
 if ck:d+=1
 if d<=0:return qs(a,be,pl)
 e=tt.get(hh);tm=0
 if e and e[0]>=d:
  if e[1]==0:return e[2]
  if e[1]==1 and e[2]>=be:return e[2]
  if e[1]==2 and e[2]<=a:return e[2]
  tm=e[3]
 if d>=3 and not ck:
  S,E,H=sd,ep,hh
  sd=-sd;ep=-1;hh^=ZS
  if E>=0:hh^=ZE[E&7]
  try:s=-sc(d-3,-be,-be+1,pl+1)
  finally:sd,ep,hh=S,E,H
  if s>=be:return be
 ms=od(gn(),tm,pl)
 bs=-MT;bm=0;fl=2
 for i,m in enumerate(ms):
  cp=mk(m)
  if at(kp[0] if sd<0 else kp[1],sd):um();continue
  try:
   if i==0:
    s=-sc(d-1,-be,-a,pl+1)
   else:
    rd=d-1-(i>3 and d>=3 and not cp and not (m>>14)&7 and not ck)
    s=-sc(rd,-a-1,-a,pl+1)
    if s>a:s=-sc(d-1,-be,-a,pl+1)
  finally:um()
  if s>bs:
   bs=s;bm=m
   if s>a:
    a=s;fl=0
    if a>=be:
     fl=1
     if not cp:kl[pl*2+1]=kl[pl*2];kl[pl*2]=m;hs[m]=hs.get(m,0)+d*d
     break
 if not bm:return -MT+pl if ck else 0
 tt[hh]=(d,fl,bs,bm)
 return bs
def rt(d,lg,a,be):
 ms=[m for m in gn() if uc(m) in lg]
 if not ms:return lg[0],a
 od(ms,tt.get(hh,(0,0,0,0))[3],0)
 bs=None;ba=a
 for m in ms:
  mk(m)
  if at(kp[0] if sd<0 else kp[1],sd):um();continue
  try:s=-sc(d-1,-be,-ba,1)
  finally:um()
  if s>ba:ba=s;bs=m
 return uc(bs) if bs is not None else lg[0],ba
def pf(fn):
 global b,sd,cs,ep,kp,hh
 b=[0]*128
 w=fn.split()
 for r,row in enumerate(w[0].split("/")):
  f=0
  for c in row:
   if c.isdigit():f+=int(c)
   else:
    s=(7-r)*16+f;v="PNBRQK".index(c.upper())+1
    b[s]=v if c.isupper() else -v
    if v==6:kp[0 if c.isupper() else 1]=s
    f+=1
 sd=1 if w[1]=="w" else -1
 cs=0
 if len(w)>2:
  for c in w[2]:cs|={"K":1,"Q":2,"k":4,"q":8}.get(c,0)
 ep=-1
 if len(w)>3 and w[3]!="-":ep=ord(w[3][0])-97+(int(w[3][1])-1)*16
 hh=0
 for i in S64:
  p=b[i]
  if p:hh^=ZP[p+6][i]
 if sd<0:hh^=ZS
 hh^=ZC[cs]
 if ep>=0:hh^=ZE[ep&7]
def po(pa,bd):
 q=U.Request(V+pa,data=json.dumps(bd).encode(),headers={"content-type":"application/json"})
 try:
  with U.urlopen(q) as r:return json.load(r)
 except E.HTTPError as x:sys.exit(f"{pa}: HTTP {x.code}")
def ch(fn,lg,mv):
 global nd,hg
 pf("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -")
 hg={hh:1}
 for u in mv:
  mk(pu(u))
  hg[hh]=hg.get(hh,0)+1
 if len(mv)<=8 or len(st)>600000:st.clear()
 pf(fn);nd=0;bs=lg[0];pv=0
 for d in range(1,64):
  try:
   w=MT if d<2 else 28+(pv*pv>>14)
   while 1:
    bs,s=rt(d,lg,pv-w,pv+w)
    if pv-w<s<pv+w:pv=s;break
    w*=2
  except A:break
  if nd>ND:break
 return bs
while True:
 g=po("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  g=po("/move",{"game":g["game"],"move":ch(g["fen"],g["legal_moves"],g["moves"])})
