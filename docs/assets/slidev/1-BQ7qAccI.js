import{p as h,A as b,B as g}from"../modules/unplugin-icons-kZaMBlYE.js";import{d as x,y as $,o as d,b as k,e as t,f as y,h as C,c as w,k as S,H as r,a6 as B,l as c,q as P,s as z}from"../modules/vue-CSlgF7c5.js";import{u,f as E}from"./context-LhTc2K18.js";import"../index-Bkx_WD9F.js";import"../monaco/bundled-types-GpUe0cbt.js";import"../modules/file-saver-igGfcqei.js";import"../modules/shiki-WYk1xoOD.js";function p(e){return e.startsWith("/")?"/Streamlit-MultiChat/"+e.slice(1):e}function H(e,o=!1){const n=e&&["#","rgb","hsl"].some(i=>e.indexOf(i)===0),s={background:n?e:void 0,color:e&&!n?"white":void 0,backgroundImage:n?void 0:e?o?`linear-gradient(#0005, #0008), url(${p(e)})`:`url("${p(e)}")`:void 0,backgroundRepeat:"no-repeat",backgroundPosition:"center",backgroundSize:"cover"};return s.background||delete s.background,s}const N={class:"my-auto w-full"},O=x({__name:"cover",props:{background:{default:"https://source.unsplash.com/collection/94734566/1920x1080"}},setup(e){u();const o=e,n=$(()=>H(o.background,!0));return(s,i)=>(d(),k("div",{class:"slidev-layout cover text-center",style:C(n.value)},[t("div",N,[y(s.$slots,"default")])],4))}}),V=t("h1",null,"Welcome to Slidev",-1),A=t("p",null,"Presentation slides for developers",-1),G={class:"pt-12"},I={class:"abs-br m-6 flex gap-2"},R={href:"https://github.com/slidevjs/slidev",target:"_blank",alt:"GitHub",title:"Open in GitHub",class:"text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white"},L={__name:"1",setup(e){const{$slidev:o,$nav:n,$clicksContext:s,$clicks:i,$page:T,$renderContext:W,$frontmatter:_}=u();return(j,a)=>{const m=h,v=b,f=g;return d(),w(O,P(z(r(E)(r(_),0))),{default:S(()=>[V,A,t("div",G,[t("span",{onClick:a[0]||(a[0]=(...l)=>r(o).nav.next&&r(o).nav.next(...l)),class:"px-2 py-1 rounded cursor-pointer",hover:"bg-white bg-opacity-10"},[B(" Press Space for next page "),c(m,{class:"inline"})])]),t("div",I,[t("button",{onClick:a[1]||(a[1]=l=>r(o).nav.openInEditor()),title:"Open in Editor",class:"text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white"},[c(v)]),t("a",R,[c(f)])])]),_:1},16)}}};export{L as default};