const __vite__mapDeps=(i,m=__vite__mapDeps,d=(m.f||(m.f=["assets/slidev/CodeRunner-Bhkxq6Ga.js","assets/modules/unplugin-icons-kZaMBlYE.js","assets/modules/vue-CSlgF7c5.js","assets/monaco/bundled-types-GpUe0cbt.js","assets/modules/file-saver-igGfcqei.js","assets/monaco/bundled-types-DSioslma.css","assets/slidev/context-LhTc2K18.js","assets/index-Bkx_WD9F.js","assets/modules/shiki-WYk1xoOD.js","assets/modules/shiki-BPvBenZD.css","assets/index-kRQC66RI.css","assets/slidev/IconButton.vue_vue_type_script_setup_true_lang-C21a9sE8.js","assets/CodeRunner-YBfxSSx9.css"])))=>i.map(i=>d[i]);
import{_ as b,o as F}from"../monaco/bundled-types-GpUe0cbt.js";import{d as U,t as l,y as V,aG as Z,ac as J,n as M,o as w,b as q,e as i,h as X,c as R,H as f,g as ee,az as te,k as oe,l as L,m as N,q as ne,s as ae,a6 as h}from"../modules/vue-CSlgF7c5.js";import{l as S}from"./lz-string-BMV4afKq.js";import{a as ie,$}from"../index-Bkx_WD9F.js";import{u as I,f as re}from"./context-LhTc2K18.js";import{I as se}from"./default-4dIDJwSV.js";import"../modules/file-saver-igGfcqei.js";import"../modules/shiki-WYk1xoOD.js";const le={class:"relative slidev-monaco-container"},de=U({__name:"Monaco",props:{codeLz:{default:""},diffLz:{},lang:{default:"typescript"},readonly:{type:Boolean,default:!1},lineNumbers:{default:"off"},height:{default:"initial"},editorOptions:{},ata:{type:Boolean,default:!0},runnable:{type:Boolean,default:!1},writable:{},autorun:{type:[Boolean,String],default:!0},showOutputAt:{type:[null,Boolean,String,Number,Array]},outputHeight:{},highlightOutput:{type:Boolean,default:!0},runnerOptions:{}},setup(z){const e=z,B=te(()=>b(()=>import("./CodeRunner-Bhkxq6Ga.js"),__vite__mapDeps([0,1,2,3,4,5,6,7,8,9,10,11,12])).then(s=>s.default)),d=l(S.decompressFromBase64(e.codeLz).trimEnd()),v=e.diffLz&&l(S.decompressFromBase64(e.diffLz).trimEnd()),E=V(()=>e.writable&&!e.readonly&&!1),u={ts:"typescript",js:"javascript"}[e.lang]??e.lang,A={typescript:"mts",javascript:"mjs",ts:"mts",js:"mjs"}[e.lang]??e.lang,m=l(),y=l(),C=l(0),r=l(),K=V(()=>e.height==="auto"?`${C.value}px`:e.height==="initial"?`${r.value}px`:e.height),O=l(),{$page:j,$renderContext:T}=I(),{currentSlideNo:Y}=ie(),G=Z(()=>Math.abs(j.value-Y.value)<=1&&O.value,s=>{["slide","presenter"].includes(T.value)?s():setTimeout(s,5e3)});return J(async()=>{const{default:s}=await b(async()=>{const{default:t}=await import("../monaco/bundled-types-GpUe0cbt.js").then(a=>a.x);return{default:t}},__vite__mapDeps([3,2,4,5])),{ata:c,monaco:o,editorOptions:H}=await s(),p=o.editor.createModel(d.value,u,o.Uri.parse(`file:///${$()}.${A}`));p.onDidChangeContent(()=>d.value=p.getValue());const k={automaticLayout:!0,readOnly:e.readonly,lineNumbers:e.lineNumbers,minimap:{enabled:!1},overviewRulerBorder:!1,overviewRulerLanes:0,padding:{top:10,bottom:10},lineNumbersMinChars:3,bracketPairColorization:{enabled:!1},tabSize:2,fontSize:11.5,fontFamily:"var(--slidev-code-font-family)",scrollBeyondLastLine:!1,...H,...e.editorOptions};let n;if(v){const t=o.editor.createModel(v.value,u,o.Uri.parse(`file:///${$()}.${A}`));t.onDidChangeContent(()=>d.value=p.getValue());const a=o.editor.createDiffEditor(y.value,{renderOverviewRuler:!1,...k});a.setModel({original:p,modified:t});const g=a.getOriginalEditor(),_=a.getModifiedEditor(),x=()=>{const D=Math.max(g.getContentHeight(),_.getContentHeight())+4;r.value??(r.value=D),C.value=D,M(()=>a.layout())};g.onDidContentSizeChange(x),_.onDidContentSizeChange(x),n=_}else{const t=o.editor.create(y.value,{model:p,lineDecorationsWidth:0,...k});t.onDidContentSizeChange(a=>{const g=a.contentHeight+4;r.value??(r.value=g),C.value=g,M(()=>n.layout())}),n=t}O.value=()=>{G(),b(()=>import("../monaco/bundled-types-GpUe0cbt.js").then(t=>t.y),__vite__mapDeps([3,2,4,5])),e.ata&&(c(n.getValue()),n.onDidChangeModelContent(F(1e3,()=>{c(n.getValue())})))};const Q=n.layoutContentWidget.bind(n);n.layoutContentWidget=t=>{Q(t),t.getId()==="editor.contrib.resizableContentHoverWidget"&&(t._resizableNode.domNode.style.transform=t._positionPreference===1?"translateY(calc(100% * (var(--slidev-slide-scale) - 1)))":"")},n.addAction({id:"slidev-save",label:"Save",keybindings:[o.KeyMod.CtrlCmd|o.KeyCode.KeyS],run:()=>{E.value,console.warn("[Slidev] this monaco editor is not writable, save action is ignored.")}}),M(()=>o.editor.remeasureFonts())}),(s,c)=>(w(),q("div",le,[i("div",{ref_key:"outer",ref:m,class:"relative slidev-monaco-container-inner",style:X({height:K.value})},[i("div",{ref_key:"container",ref:y,class:"absolute inset-0.5"},null,512)],4),e.runnable?(w(),R(f(B),{key:0,modelValue:d.value,"onUpdate:modelValue":c[0]||(c[0]=o=>d.value=o),lang:f(u),autorun:e.autorun,"show-output-at":e.showOutputAt,height:e.outputHeight,"highlight-output":e.highlightOutput,"runner-options":e.runnerOptions},null,8,["modelValue","lang","autorun","show-output-at","height","highlight-output","runner-options"])):ee("",!0)]))}}),ue=i("h1",null,"Monaco Editor",-1),ce=i("p",null,"Slidev provides built-in Monaco Editor support.",-1),pe=i("p",null,[h("Add "),i("code",null,"{monaco}"),h(" to the code block to turn it into an editor:")],-1),ge=i("p",null,[h("Use "),i("code",null,"{monaco-run}"),h(" to create an editor that can execute the code directly in the slide:")],-1),be={__name:"15",setup(z){const{$slidev:e,$nav:B,$clicksContext:d,$clicks:v,$page:E,$renderContext:P,$frontmatter:u}=I();return(W,A)=>{const m=de;return w(),R(se,ne(ae(f(re)(f(u),14))),{default:oe(()=>[ue,ce,pe,L(m,N({"code-lz":"JYWwDg9gTgLgBAbzlApgMzgXzmqERwDkAbgK4qEBQoksicK4MAngIJRQCGzWOeBhAHQB6FAA8YKKADtOAGyqUAxhGkBneJw5wAvMnQAKRmBbsuzAwEYADAEpblIA",lang:"ts"},{}),null,16),ge,L(m,N({runnable:"","code-lz":"JYWwDg9gTgLgBAbzgNwKZQM7AgOzgXzgDMoIQ4ByZAV1QoChRJZE5VwYBPAQSigENOAGjgZBACVQAbKRALFS5CgDoA9KgAeMdDn5SG9MZ0kyIACgCU9AMa4MEKamWyA5mYAGNVHAAkCNJjYOPjuVrY49o7OEG7sYFy8ApwAPDjUIABG6AB8ZgCMAAwWylCoACbU1qhmRMAZcAC82XAA2srttRkincr8MGYAtHkWAIRwANTEdb39AwBMowC6Ii15InmLFlZAA",lang:"ts"},{}),null,16)]),_:1},16)}}};export{be as default};