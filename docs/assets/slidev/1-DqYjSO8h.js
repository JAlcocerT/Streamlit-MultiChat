import{p as f,A as b,B as g}from"../modules/unplugin-icons-BSfgU0VP.js";import{d as x,y as k,o as u,b as $,e,f as y,h as C,c as w,k as S,A as r,a6 as B,l as c,q as A,s as P}from"../modules/vue-CF22wb2R.js";import{u as d,f as M}from"./context-DDKcMwaC.js";import"../index-KiKyF8R1.js";import"../modules/shiki-Dk8qO-MX.js";function p(t){return t.startsWith("/")?"/Streamlit-Multichat"+t.slice(1):t}function z(t,o=!1){const n=t&&["#","rgb","hsl"].some(i=>t.indexOf(i)===0),s={background:n?t:void 0,color:t&&!n?"white":void 0,backgroundImage:n?void 0:t?o?`linear-gradient(#0005, #0008), url(${p(t)})`:`url("${p(t)}")`:void 0,backgroundRepeat:"no-repeat",backgroundPosition:"center",backgroundSize:"cover"};return s.background||delete s.background,s}const E={class:"my-auto w-full"},N=x({__name:"cover",props:{background:{default:"https://source.unsplash.com/collection/94734566/1920x1080"}},setup(t){d();const o=t,n=k(()=>z(o.background,!0));return(s,i)=>(u(),$("div",{class:"slidev-layout cover text-center",style:C(n.value)},[e("div",E,[y(s.$slots,"default")])],4))}}),O=e("h1",null,"Streamlit MultiChat",-1),T=e("p",null,"Chat with multiple LLMs from one App.",-1),V={class:"pt-12"},G={class:"abs-br m-6 flex gap-2"},H={href:"https://github.com/JAlcocerT/Streamlit-Multichat",target:"_blank",alt:"GitHub",title:"Open in GitHub",class:"text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white"},D={__name:"1",setup(t){const{$slidev:o,$nav:n,$clicksContext:s,$clicks:i,$page:I,$renderContext:L,$frontmatter:_}=d();return(R,a)=>{const m=f,h=b,v=g;return u(),w(N,A(P(r(M)(r(_),0))),{default:S(()=>[O,T,e("div",V,[e("span",{onClick:a[0]||(a[0]=(...l)=>r(o).nav.next&&r(o).nav.next(...l)),class:"px-2 py-1 rounded cursor-pointer",hover:"bg-white bg-opacity-10"},[B(" Press Space and Check how it's built "),c(m,{class:"inline"})])]),e("div",G,[e("button",{onClick:a[1]||(a[1]=l=>r(o).nav.openInEditor()),title:"Open in Editor",class:"text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white"},[c(h)]),e("a",H,[c(v)])])]),_:1},16)}}};export{D as default};
