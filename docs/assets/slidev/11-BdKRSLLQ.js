import{d as A,t as E,aB as L,ac as C,y as b,E as R,o as e,b as l,f as H,c as $,k as M,l as I,m as T,e as s,q as P,s as Y,H as S,a6 as v}from"../modules/vue-CSlgF7c5.js";import{$ as q,C as N,a2 as K,a3 as V,a4 as X}from"../index-Bkx_WD9F.js";import{u as k,f as J}from"./context-LhTc2K18.js";import{I as D}from"./default-4dIDJwSV.js";import"../monaco/bundled-types-GpUe0cbt.js";import"../modules/file-saver-igGfcqei.js";import"../modules/shiki-WYk1xoOD.js";const W=A({__name:"KaTexBlockWrapper",props:{ranges:{type:Array,default:()=>[]},finally:{type:[String,Number],default:"last"},startLine:{type:Number,default:1},at:{type:[String,Number],default:"+1"}},setup(w){const t=w,{$clicksContext:a}=k(),o=E(),g=q();return L(()=>{a.unregister(g)}),C(()=>{var u;if(!a||!((u=t.ranges)!=null&&u.length))return;const n=a.calculateSince(t.at,t.ranges.length-1);a.register(g,n);const h=b(()=>n?Math.max(0,a.current-n.start+1):N),r=b(()=>t.finally==="last"?t.ranges.at(-1):t.finally.toString());R(()=>{if(!o.value)return;let _=t.ranges[h.value]??r.value;const d=_==="hide";o.value.classList.toggle(K,d),d&&(_=t.ranges[h.value+1]??r.value);const f=o.value.querySelectorAll(".mtable > [class*=col-align]");if(!f)return;const z=Array.from(f).map(m=>Array.from(m.querySelectorAll(":scope > .vlist-t > .vlist-r > .vlist > span > .mord"))),i=[];for(const m of z)m.forEach((p,c)=>{p&&(Array.isArray(i[c])?i[c].push(p):i[c]=[p])});const x=t.startLine,B=V(i.length+x-1,_);i.forEach((m,p)=>{const c=B.includes(p+x);m.forEach(y=>{y.classList.toggle(X,!0),y.classList.toggle("highlighted",c),y.classList.toggle("dishonored",!c)})})})}),(n,h)=>(e(),l("div",{ref_key:"el",ref:o,class:"slidev-katex-wrapper"},[H(n.$slots,"default")],512))}}),j=s("h1",null,"LaTeX",-1),G=s("p",null,[v("LaTeX is supported out-of-box. Powered by "),s("a",{href:"https://katex.org/",target:"_blank"},"KaTeX"),v(".")],-1),O=s("div",{"h-3":""},null,-1),U=s("p",null,[v("Inline "),s("span",{class:"katex"},[s("span",{class:"katex-mathml"},[s("math",{xmlns:"http://www.w3.org/1998/Math/MathML"},[s("semantics",null,[s("mrow",null,[s("msqrt",null,[s("mrow",null,[s("mn",null,"3"),s("mi",null,"x"),s("mo",null,"−"),s("mn",null,"1")])]),s("mo",null,"+"),s("mo",{stretchy:"false"},"("),s("mn",null,"1"),s("mo",null,"+"),s("mi",null,"x"),s("msup",null,[s("mo",{stretchy:"false"},")"),s("mn",null,"2")])]),s("annotation",{encoding:"application/x-tex"},"\\sqrt{3x-1}+(1+x)^2")])])]),s("span",{class:"katex-html","aria-hidden":"true"},[s("span",{class:"base"},[s("span",{class:"strut",style:{height:"1.04em","vertical-align":"-0.1744em"}}),s("span",{class:"mord sqrt"},[s("span",{class:"vlist-t vlist-t2"},[s("span",{class:"vlist-r"},[s("span",{class:"vlist",style:{height:"0.8656em"}},[s("span",{class:"svg-align",style:{top:"-3em"}},[s("span",{class:"pstrut",style:{height:"3em"}}),s("span",{class:"mord",style:{"padding-left":"0.833em"}},[s("span",{class:"mord"},"3"),s("span",{class:"mord mathnormal"},"x"),s("span",{class:"mspace",style:{"margin-right":"0.2222em"}}),s("span",{class:"mbin"},"−"),s("span",{class:"mspace",style:{"margin-right":"0.2222em"}}),s("span",{class:"mord"},"1")])]),s("span",{style:{top:"-2.8256em"}},[s("span",{class:"pstrut",style:{height:"3em"}}),s("span",{class:"hide-tail",style:{"min-width":"0.853em",height:"1.08em"}},[s("svg",{xmlns:"http://www.w3.org/2000/svg",width:"400em",height:"1.08em",viewBox:"0 0 400000 1080",preserveAspectRatio:"xMinYMin slice"},[s("path",{d:`M95,702
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l0 -0
c5.3,-9.3,12,-14,20,-14
H400000v40H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M834 80h400000v40h-400000z`})])])])]),s("span",{class:"vlist-s"},"​")]),s("span",{class:"vlist-r"},[s("span",{class:"vlist",style:{height:"0.1744em"}},[s("span")])])])]),s("span",{class:"mspace",style:{"margin-right":"0.2222em"}}),s("span",{class:"mbin"},"+"),s("span",{class:"mspace",style:{"margin-right":"0.2222em"}})]),s("span",{class:"base"},[s("span",{class:"strut",style:{height:"1em","vertical-align":"-0.25em"}}),s("span",{class:"mopen"},"("),s("span",{class:"mord"},"1"),s("span",{class:"mspace",style:{"margin-right":"0.2222em"}}),s("span",{class:"mbin"},"+"),s("span",{class:"mspace",style:{"margin-right":"0.2222em"}})]),s("span",{class:"base"},[s("span",{class:"strut",style:{height:"1.0641em","vertical-align":"-0.25em"}}),s("span",{class:"mord mathnormal"},"x"),s("span",{class:"mclose"},[s("span",{class:"mclose"},")"),s("span",{class:"msupsub"},[s("span",{class:"vlist-t"},[s("span",{class:"vlist-r"},[s("span",{class:"vlist",style:{height:"0.8141em"}},[s("span",{style:{top:"-3.063em","margin-right":"0.05em"}},[s("span",{class:"pstrut",style:{height:"2.7em"}}),s("span",{class:"sizing reset-size6 size3 mtight"},[s("span",{class:"mord mtight"},"2")])])])])])])])])])])],-1),F=s("p",null,"Block",-1),Q={class:"katex-display"},Z={class:"katex"},ss=s("span",{class:"katex-mathml"},[s("math",{xmlns:"http://www.w3.org/1998/Math/MathML",display:"block"},[s("semantics",null,[s("mtable",{rowspacing:"0.25em",columnalign:"right left",columnspacing:"0em"},[s("mtr",null,[s("mtd",null,[s("mstyle",{scriptlevel:"0",displaystyle:"true"},[s("mrow",null,[s("mi",{mathvariant:"normal"},"∇"),s("mo",null,"⋅"),s("mover",{accent:"true"},[s("mi",null,"E"),s("mo",null,"⃗")])])])]),s("mtd",null,[s("mstyle",{scriptlevel:"0",displaystyle:"true"},[s("mrow",null,[s("mrow"),s("mo",null,"="),s("mfrac",null,[s("mi",null,"ρ"),s("msub",null,[s("mi",null,"ε"),s("mn",null,"0")])])])])])]),s("mtr",null,[s("mtd",null,[s("mstyle",{scriptlevel:"0",displaystyle:"true"},[s("mrow",null,[s("mi",{mathvariant:"normal"},"∇"),s("mo",null,"⋅"),s("mover",{accent:"true"},[s("mi",null,"B"),s("mo",null,"⃗")])])])]),s("mtd",null,[s("mstyle",{scriptlevel:"0",displaystyle:"true"},[s("mrow",null,[s("mrow"),s("mo",null,"="),s("mn",null,"0")])])])]),s("mtr",null,[s("mtd",null,[s("mstyle",{scriptlevel:"0",displaystyle:"true"},[s("mrow",null,[s("mi",{mathvariant:"normal"},"∇"),s("mo",null,"×"),s("mover",{accent:"true"},[s("mi",null,"E"),s("mo",null,"⃗")])])])]),s("mtd",null,[s("mstyle",{scriptlevel:"0",displaystyle:"true"},[s("mrow",null,[s("mrow"),s("mo",null,"="),s("mo",null,"−"),s("mfrac",null,[s("mrow",null,[s("mi",{mathvariant:"normal"},"∂"),s("mover",{accent:"true"},[s("mi",null,"B"),s("mo",null,"⃗")])]),s("mrow",null,[s("mi",{mathvariant:"normal"},"∂"),s("mi",null,"t")])])])])])]),s("mtr",null,[s("mtd",null,[s("mstyle",{scriptlevel:"0",displaystyle:"true"},[s("mrow",null,[s("mi",{mathvariant:"normal"},"∇"),s("mo",null,"×"),s("mover",{accent:"true"},[s("mi",null,"B"),s("mo",null,"⃗")])])])]),s("mtd",null,[s("mstyle",{scriptlevel:"0",displaystyle:"true"},[s("mrow",null,[s("mrow"),s("mo",null,"="),s("msub",null,[s("mi",null,"μ"),s("mn",null,"0")]),s("mover",{accent:"true"},[s("mi",null,"J"),s("mo",null,"⃗")]),s("mo",null,"+"),s("msub",null,[s("mi",null,"μ"),s("mn",null,"0")]),s("msub",null,[s("mi",null,"ε"),s("mn",null,"0")]),s("mfrac",null,[s("mrow",null,[s("mi",{mathvariant:"normal"},"∂"),s("mover",{accent:"true"},[s("mi",null,"E"),s("mo",null,"⃗")])]),s("mrow",null,[s("mi",{mathvariant:"normal"},"∂"),s("mi",null,"t")])])])])])])]),s("annotation",{encoding:"application/x-tex"},"\\begin{aligned} \\nabla \\cdot \\vec{E} &= \\frac{\\rho}{\\varepsilon_0} \\\\ \\nabla \\cdot \\vec{B} &= 0 \\\\ \\nabla \\times \\vec{E} &= -\\frac{\\partial\\vec{B}}{\\partial t} \\\\ \\nabla \\times \\vec{B} &= \\mu_0\\vec{J} + \\mu_0\\varepsilon_0\\frac{\\partial\\vec{E}}{\\partial t} \\end{aligned} ")])])],-1),ts={class:"katex-html","aria-hidden":"true"},es={class:"base"},ls=s("span",{class:"strut",style:{height:"9.1286em","vertical-align":"-4.3143em"}},null,-1),as={class:"mord"},ns={class:"mtable"},cs={class:"col-align-r"},os={class:"vlist-t vlist-t2"},is={class:"vlist-r"},ms={class:"vlist",style:{height:"4.8143em"}},ps={style:{top:"-7.35em"}},hs=s("span",{class:"pstrut",style:{height:"3.6433em"}},null,-1),rs={class:"mord"},_s=s("span",{class:"mord"},"∇",-1),ds=s("span",{class:"mspace",style:{"margin-right":"0.2222em"}},null,-1),gs=s("span",{class:"mbin"},"⋅",-1),us=s("span",{class:"mspace",style:{"margin-right":"0.2222em"}},null,-1),ys={class:"mord accent"},vs={class:"vlist-t"},ws={class:"vlist-r"},fs={class:"vlist",style:{height:"0.9663em"}},xs=s("span",{style:{top:"-3em"}},[s("span",{class:"pstrut",style:{height:"3em"}}),s("span",{class:"mord mathnormal",style:{"margin-right":"0.05764em"}},"E")],-1),bs={style:{top:"-3.2523em"}},Ms=s("span",{class:"pstrut",style:{height:"3em"}},null,-1),Ss={class:"accent-body",style:{left:"-0.1522em"}},ks={class:"overlay",style:{height:"0.714em",width:"0.471em"}},zs={xmlns:"http://www.w3.org/2000/svg",width:"0.471em",height:"0.714em",style:{width:"0.471em"},viewBox:"0 0 471 714",preserveAspectRatio:"xMinYMin"},Bs=s("path",{d:`M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5
3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11
10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63
-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1
-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59
H213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359
c-16-25.333-24-45-24-59z`},null,-1),As=[Bs],Es={style:{top:"-5.2477em"}},Ls=s("span",{class:"pstrut",style:{height:"3.6433em"}},null,-1),Cs={class:"mord"},Rs=s("span",{class:"mord"},"∇",-1),Hs=s("span",{class:"mspace",style:{"margin-right":"0.2222em"}},null,-1),$s=s("span",{class:"mbin"},"⋅",-1),Is=s("span",{class:"mspace",style:{"margin-right":"0.2222em"}},null,-1),Ts={class:"mord accent"},Ps={class:"vlist-t"},Ys={class:"vlist-r"},qs={class:"vlist",style:{height:"0.9663em"}},Ns=s("span",{style:{top:"-3em"}},[s("span",{class:"pstrut",style:{height:"3em"}}),s("span",{class:"mord mathnormal",style:{"margin-right":"0.05017em"}},"B")],-1),Ks={style:{top:"-3.2523em"}},Vs=s("span",{class:"pstrut",style:{height:"3em"}},null,-1),Xs={class:"accent-body",style:{left:"-0.1522em"}},Js={class:"overlay",style:{height:"0.714em",width:"0.471em"}},Ds={xmlns:"http://www.w3.org/2000/svg",width:"0.471em",height:"0.714em",style:{width:"0.471em"},viewBox:"0 0 471 714",preserveAspectRatio:"xMinYMin"},Ws=s("path",{d:`M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5
3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11
10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63
-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1
-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59
H213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359
c-16-25.333-24-45-24-59z`},null,-1),js=[Ws],Gs={style:{top:"-2.9444em"}},Os=s("span",{class:"pstrut",style:{height:"3.6433em"}},null,-1),Us={class:"mord"},Fs=s("span",{class:"mord"},"∇",-1),Qs=s("span",{class:"mspace",style:{"margin-right":"0.2222em"}},null,-1),Zs=s("span",{class:"mbin"},"×",-1),st=s("span",{class:"mspace",style:{"margin-right":"0.2222em"}},null,-1),tt={class:"mord accent"},et={class:"vlist-t"},lt={class:"vlist-r"},at={class:"vlist",style:{height:"0.9663em"}},nt=s("span",{style:{top:"-3em"}},[s("span",{class:"pstrut",style:{height:"3em"}}),s("span",{class:"mord mathnormal",style:{"margin-right":"0.05764em"}},"E")],-1),ct={style:{top:"-3.2523em"}},ot=s("span",{class:"pstrut",style:{height:"3em"}},null,-1),it={class:"accent-body",style:{left:"-0.1522em"}},mt={class:"overlay",style:{height:"0.714em",width:"0.471em"}},pt={xmlns:"http://www.w3.org/2000/svg",width:"0.471em",height:"0.714em",style:{width:"0.471em"},viewBox:"0 0 471 714",preserveAspectRatio:"xMinYMin"},ht=s("path",{d:`M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5
3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11
10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63
-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1
-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59
H213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359
c-16-25.333-24-45-24-59z`},null,-1),rt=[ht],_t={style:{top:"-0.3151em"}},dt=s("span",{class:"pstrut",style:{height:"3.6433em"}},null,-1),gt={class:"mord"},ut=s("span",{class:"mord"},"∇",-1),yt=s("span",{class:"mspace",style:{"margin-right":"0.2222em"}},null,-1),vt=s("span",{class:"mbin"},"×",-1),wt=s("span",{class:"mspace",style:{"margin-right":"0.2222em"}},null,-1),ft={class:"mord accent"},xt={class:"vlist-t"},bt={class:"vlist-r"},Mt={class:"vlist",style:{height:"0.9663em"}},St=s("span",{style:{top:"-3em"}},[s("span",{class:"pstrut",style:{height:"3em"}}),s("span",{class:"mord mathnormal",style:{"margin-right":"0.05017em"}},"B")],-1),kt={style:{top:"-3.2523em"}},zt=s("span",{class:"pstrut",style:{height:"3em"}},null,-1),Bt={class:"accent-body",style:{left:"-0.1522em"}},At={class:"overlay",style:{height:"0.714em",width:"0.471em"}},Et={xmlns:"http://www.w3.org/2000/svg",width:"0.471em",height:"0.714em",style:{width:"0.471em"},viewBox:"0 0 471 714",preserveAspectRatio:"xMinYMin"},Lt=s("path",{d:`M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5
3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11
10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63
-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1
-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59
H213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359
c-16-25.333-24-45-24-59z`},null,-1),Ct=[Lt],Rt=s("span",{class:"vlist-s"},"​",-1),Ht=s("span",{class:"vlist-r"},[s("span",{class:"vlist",style:{height:"4.3143em"}},[s("span")])],-1),$t={class:"col-align-l"},It={class:"vlist-t vlist-t2"},Tt={class:"vlist-r"},Pt={class:"vlist",style:{height:"4.8143em"}},Yt=s("span",{style:{top:"-7.35em"}},[s("span",{class:"pstrut",style:{height:"3.6433em"}}),s("span",{class:"mord"},[s("span",{class:"mord"}),s("span",{class:"mspace",style:{"margin-right":"0.2778em"}}),s("span",{class:"mrel"},"="),s("span",{class:"mspace",style:{"margin-right":"0.2778em"}}),s("span",{class:"mord"},[s("span",{class:"mopen nulldelimiter"}),s("span",{class:"mfrac"},[s("span",{class:"vlist-t vlist-t2"},[s("span",{class:"vlist-r"},[s("span",{class:"vlist",style:{height:"1.1076em"}},[s("span",{style:{top:"-2.314em"}},[s("span",{class:"pstrut",style:{height:"3em"}}),s("span",{class:"mord"},[s("span",{class:"mord"},[s("span",{class:"mord mathnormal"},"ε"),s("span",{class:"msupsub"},[s("span",{class:"vlist-t vlist-t2"},[s("span",{class:"vlist-r"},[s("span",{class:"vlist",style:{height:"0.3011em"}},[s("span",{style:{top:"-2.55em","margin-left":"0em","margin-right":"0.05em"}},[s("span",{class:"pstrut",style:{height:"2.7em"}}),s("span",{class:"sizing reset-size6 size3 mtight"},[s("span",{class:"mord mtight"},"0")])])]),s("span",{class:"vlist-s"},"​")]),s("span",{class:"vlist-r"},[s("span",{class:"vlist",style:{height:"0.15em"}},[s("span")])])])])])])]),s("span",{style:{top:"-3.23em"}},[s("span",{class:"pstrut",style:{height:"3em"}}),s("span",{class:"frac-line",style:{"border-bottom-width":"0.04em"}})]),s("span",{style:{top:"-3.677em"}},[s("span",{class:"pstrut",style:{height:"3em"}}),s("span",{class:"mord"},[s("span",{class:"mord mathnormal"},"ρ")])])]),s("span",{class:"vlist-s"},"​")]),s("span",{class:"vlist-r"},[s("span",{class:"vlist",style:{height:"0.836em"}},[s("span")])])])]),s("span",{class:"mclose nulldelimiter"})])])],-1),qt=s("span",{style:{top:"-5.2477em"}},[s("span",{class:"pstrut",style:{height:"3.6433em"}}),s("span",{class:"mord"},[s("span",{class:"mord"}),s("span",{class:"mspace",style:{"margin-right":"0.2778em"}}),s("span",{class:"mrel"},"="),s("span",{class:"mspace",style:{"margin-right":"0.2778em"}}),s("span",{class:"mord"},"0")])],-1),Nt={style:{top:"-2.9444em"}},Kt=s("span",{class:"pstrut",style:{height:"3.6433em"}},null,-1),Vt={class:"mord"},Xt=s("span",{class:"mord"},null,-1),Jt=s("span",{class:"mspace",style:{"margin-right":"0.2778em"}},null,-1),Dt=s("span",{class:"mrel"},"=",-1),Wt=s("span",{class:"mspace",style:{"margin-right":"0.2778em"}},null,-1),jt=s("span",{class:"mord"},"−",-1),Gt={class:"mord"},Ot=s("span",{class:"mopen nulldelimiter"},null,-1),Ut={class:"mfrac"},Ft={class:"vlist-t vlist-t2"},Qt={class:"vlist-r"},Zt={class:"vlist",style:{height:"1.6433em"}},se=s("span",{style:{top:"-2.314em"}},[s("span",{class:"pstrut",style:{height:"3em"}}),s("span",{class:"mord"},[s("span",{class:"mord",style:{"margin-right":"0.05556em"}},"∂"),s("span",{class:"mord mathnormal"},"t")])],-1),te=s("span",{style:{top:"-3.23em"}},[s("span",{class:"pstrut",style:{height:"3em"}}),s("span",{class:"frac-line",style:{"border-bottom-width":"0.04em"}})],-1),ee={style:{top:"-3.677em"}},le=s("span",{class:"pstrut",style:{height:"3em"}},null,-1),ae={class:"mord"},ne=s("span",{class:"mord",style:{"margin-right":"0.05556em"}},"∂",-1),ce={class:"mord accent"},oe={class:"vlist-t"},ie={class:"vlist-r"},me={class:"vlist",style:{height:"0.9663em"}},pe=s("span",{style:{top:"-3em"}},[s("span",{class:"pstrut",style:{height:"3em"}}),s("span",{class:"mord mathnormal",style:{"margin-right":"0.05017em"}},"B")],-1),he={style:{top:"-3.2523em"}},re=s("span",{class:"pstrut",style:{height:"3em"}},null,-1),_e={class:"accent-body",style:{left:"-0.1522em"}},de={class:"overlay",style:{height:"0.714em",width:"0.471em"}},ge={xmlns:"http://www.w3.org/2000/svg",width:"0.471em",height:"0.714em",style:{width:"0.471em"},viewBox:"0 0 471 714",preserveAspectRatio:"xMinYMin"},ue=s("path",{d:`M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5
3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11
10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63
-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1
-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59
H213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359
c-16-25.333-24-45-24-59z`},null,-1),ye=[ue],ve=s("span",{class:"vlist-s"},"​",-1),we=s("span",{class:"vlist-r"},[s("span",{class:"vlist",style:{height:"0.686em"}},[s("span")])],-1),fe=s("span",{class:"mclose nulldelimiter"},null,-1),xe={style:{top:"-0.3151em"}},be=s("span",{class:"pstrut",style:{height:"3.6433em"}},null,-1),Me={class:"mord"},Se=s("span",{class:"mord"},null,-1),ke=s("span",{class:"mspace",style:{"margin-right":"0.2778em"}},null,-1),ze=s("span",{class:"mrel"},"=",-1),Be=s("span",{class:"mspace",style:{"margin-right":"0.2778em"}},null,-1),Ae=s("span",{class:"mord"},[s("span",{class:"mord mathnormal"},"μ"),s("span",{class:"msupsub"},[s("span",{class:"vlist-t vlist-t2"},[s("span",{class:"vlist-r"},[s("span",{class:"vlist",style:{height:"0.3011em"}},[s("span",{style:{top:"-2.55em","margin-left":"0em","margin-right":"0.05em"}},[s("span",{class:"pstrut",style:{height:"2.7em"}}),s("span",{class:"sizing reset-size6 size3 mtight"},[s("span",{class:"mord mtight"},"0")])])]),s("span",{class:"vlist-s"},"​")]),s("span",{class:"vlist-r"},[s("span",{class:"vlist",style:{height:"0.15em"}},[s("span")])])])])],-1),Ee={class:"mord accent"},Le={class:"vlist-t"},Ce={class:"vlist-r"},Re={class:"vlist",style:{height:"0.9663em"}},He=s("span",{style:{top:"-3em"}},[s("span",{class:"pstrut",style:{height:"3em"}}),s("span",{class:"mord mathnormal",style:{"margin-right":"0.09618em"}},"J")],-1),$e={style:{top:"-3.2523em"}},Ie=s("span",{class:"pstrut",style:{height:"3em"}},null,-1),Te={class:"accent-body",style:{left:"-0.0688em"}},Pe={class:"overlay",style:{height:"0.714em",width:"0.471em"}},Ye={xmlns:"http://www.w3.org/2000/svg",width:"0.471em",height:"0.714em",style:{width:"0.471em"},viewBox:"0 0 471 714",preserveAspectRatio:"xMinYMin"},qe=s("path",{d:`M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5
3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11
10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63
-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1
-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59
H213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359
c-16-25.333-24-45-24-59z`},null,-1),Ne=[qe],Ke=s("span",{class:"mspace",style:{"margin-right":"0.2222em"}},null,-1),Ve=s("span",{class:"mbin"},"+",-1),Xe=s("span",{class:"mspace",style:{"margin-right":"0.2222em"}},null,-1),Je=s("span",{class:"mord"},[s("span",{class:"mord mathnormal"},"μ"),s("span",{class:"msupsub"},[s("span",{class:"vlist-t vlist-t2"},[s("span",{class:"vlist-r"},[s("span",{class:"vlist",style:{height:"0.3011em"}},[s("span",{style:{top:"-2.55em","margin-left":"0em","margin-right":"0.05em"}},[s("span",{class:"pstrut",style:{height:"2.7em"}}),s("span",{class:"sizing reset-size6 size3 mtight"},[s("span",{class:"mord mtight"},"0")])])]),s("span",{class:"vlist-s"},"​")]),s("span",{class:"vlist-r"},[s("span",{class:"vlist",style:{height:"0.15em"}},[s("span")])])])])],-1),De=s("span",{class:"mord"},[s("span",{class:"mord mathnormal"},"ε"),s("span",{class:"msupsub"},[s("span",{class:"vlist-t vlist-t2"},[s("span",{class:"vlist-r"},[s("span",{class:"vlist",style:{height:"0.3011em"}},[s("span",{style:{top:"-2.55em","margin-left":"0em","margin-right":"0.05em"}},[s("span",{class:"pstrut",style:{height:"2.7em"}}),s("span",{class:"sizing reset-size6 size3 mtight"},[s("span",{class:"mord mtight"},"0")])])]),s("span",{class:"vlist-s"},"​")]),s("span",{class:"vlist-r"},[s("span",{class:"vlist",style:{height:"0.15em"}},[s("span")])])])])],-1),We={class:"mord"},je=s("span",{class:"mopen nulldelimiter"},null,-1),Ge={class:"mfrac"},Oe={class:"vlist-t vlist-t2"},Ue={class:"vlist-r"},Fe={class:"vlist",style:{height:"1.6433em"}},Qe=s("span",{style:{top:"-2.314em"}},[s("span",{class:"pstrut",style:{height:"3em"}}),s("span",{class:"mord"},[s("span",{class:"mord",style:{"margin-right":"0.05556em"}},"∂"),s("span",{class:"mord mathnormal"},"t")])],-1),Ze=s("span",{style:{top:"-3.23em"}},[s("span",{class:"pstrut",style:{height:"3em"}}),s("span",{class:"frac-line",style:{"border-bottom-width":"0.04em"}})],-1),sl={style:{top:"-3.677em"}},tl=s("span",{class:"pstrut",style:{height:"3em"}},null,-1),el={class:"mord"},ll=s("span",{class:"mord",style:{"margin-right":"0.05556em"}},"∂",-1),al={class:"mord accent"},nl={class:"vlist-t"},cl={class:"vlist-r"},ol={class:"vlist",style:{height:"0.9663em"}},il=s("span",{style:{top:"-3em"}},[s("span",{class:"pstrut",style:{height:"3em"}}),s("span",{class:"mord mathnormal",style:{"margin-right":"0.05764em"}},"E")],-1),ml={style:{top:"-3.2523em"}},pl=s("span",{class:"pstrut",style:{height:"3em"}},null,-1),hl={class:"accent-body",style:{left:"-0.1522em"}},rl={class:"overlay",style:{height:"0.714em",width:"0.471em"}},_l={xmlns:"http://www.w3.org/2000/svg",width:"0.471em",height:"0.714em",style:{width:"0.471em"},viewBox:"0 0 471 714",preserveAspectRatio:"xMinYMin"},dl=s("path",{d:`M377 20c0-5.333 1.833-10 5.5-14S391 0 397 0c4.667 0 8.667 1.667 12 5
3.333 2.667 6.667 9 10 19 6.667 24.667 20.333 43.667 41 57 7.333 4.667 11
10.667 11 18 0 6-1 10-3 12s-6.667 5-14 9c-28.667 14.667-53.667 35.667-75 63
-1.333 1.333-3.167 3.5-5.5 6.5s-4 4.833-5 5.5c-1 .667-2.5 1.333-4.5 2s-4.333 1
-7 1c-4.667 0-9.167-1.833-13.5-5.5S337 184 337 178c0-12.667 15.667-32.333 47-59
H213l-171-1c-8.667-6-13-12.333-13-19 0-4.667 4.333-11.333 13-20h359
c-16-25.333-24-45-24-59z`},null,-1),gl=[dl],ul=s("span",{class:"vlist-s"},"​",-1),yl=s("span",{class:"vlist-r"},[s("span",{class:"vlist",style:{height:"0.686em"}},[s("span")])],-1),vl=s("span",{class:"mclose nulldelimiter"},null,-1),wl=s("span",{class:"vlist-s"},"​",-1),fl=s("span",{class:"vlist-r"},[s("span",{class:"vlist",style:{height:"4.3143em"}},[s("span")])],-1),xl=s("p",null,[s("a",{href:"https://sli.dev/guide/syntax#latex",target:"_blank"},"Learn more")],-1),El={__name:"11",setup(w){const{$slidev:t,$nav:a,$clicksContext:o,$clicks:g,$page:n,$renderContext:h,$frontmatter:r}=k();return(u,_)=>{const d=W;return e(),$(D,P(Y(S(J)(S(r),10))),{default:M(()=>[j,G,O,U,F,I(d,T({},{ranges:["1","3","all"]}),{default:M(()=>[s("p",null,[s("span",Q,[s("span",Z,[ss,s("span",ts,[s("span",es,[ls,s("span",as,[s("span",ns,[s("span",cs,[s("span",os,[s("span",is,[s("span",ms,[s("span",ps,[hs,s("span",rs,[_s,ds,gs,us,s("span",ys,[s("span",vs,[s("span",ws,[s("span",fs,[xs,s("span",bs,[Ms,s("span",Ss,[s("span",ks,[(e(),l("svg",zs,As))])])])])])])])])]),s("span",Es,[Ls,s("span",Cs,[Rs,Hs,$s,Is,s("span",Ts,[s("span",Ps,[s("span",Ys,[s("span",qs,[Ns,s("span",Ks,[Vs,s("span",Xs,[s("span",Js,[(e(),l("svg",Ds,js))])])])])])])])])]),s("span",Gs,[Os,s("span",Us,[Fs,Qs,Zs,st,s("span",tt,[s("span",et,[s("span",lt,[s("span",at,[nt,s("span",ct,[ot,s("span",it,[s("span",mt,[(e(),l("svg",pt,rt))])])])])])])])])]),s("span",_t,[dt,s("span",gt,[ut,yt,vt,wt,s("span",ft,[s("span",xt,[s("span",bt,[s("span",Mt,[St,s("span",kt,[zt,s("span",Bt,[s("span",At,[(e(),l("svg",Et,Ct))])])])])])])])])])]),Rt]),Ht])]),s("span",$t,[s("span",It,[s("span",Tt,[s("span",Pt,[Yt,qt,s("span",Nt,[Kt,s("span",Vt,[Xt,Jt,Dt,Wt,jt,s("span",Gt,[Ot,s("span",Ut,[s("span",Ft,[s("span",Qt,[s("span",Zt,[se,te,s("span",ee,[le,s("span",ae,[ne,s("span",ce,[s("span",oe,[s("span",ie,[s("span",me,[pe,s("span",he,[re,s("span",_e,[s("span",de,[(e(),l("svg",ge,ye))])])])])])])])])])]),ve]),we])]),fe])])]),s("span",xe,[be,s("span",Me,[Se,ke,ze,Be,Ae,s("span",Ee,[s("span",Le,[s("span",Ce,[s("span",Re,[He,s("span",$e,[Ie,s("span",Te,[s("span",Pe,[(e(),l("svg",Ye,Ne))])])])])])])]),Ke,Ve,Xe,Je,De,s("span",We,[je,s("span",Ge,[s("span",Oe,[s("span",Ue,[s("span",Fe,[Qe,Ze,s("span",sl,[tl,s("span",el,[ll,s("span",al,[s("span",nl,[s("span",cl,[s("span",ol,[il,s("span",ml,[pl,s("span",hl,[s("span",rl,[(e(),l("svg",_l,gl))])])])])])])])])])]),ul]),yl])]),vl])])])]),wl]),fl])])])])])])])])])]),_:1},16),xl]),_:1},16)}}};export{El as default};