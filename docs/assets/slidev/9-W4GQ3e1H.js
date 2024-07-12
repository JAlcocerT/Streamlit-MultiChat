import{d as y,y as A,o as r,b as g,f as D,h as B,t as u,ac as $,c as v,k as m,e as s,l as _,x,g as k,m as b,q as T,s as E,A as f,a6 as h}from"../modules/vue-DQa2LXgQ.js";import{C as S}from"../modules/unplugin-icons-BR8hrWPm.js";import{b as N}from"../index-IRPrl4M6.js";import{_ as M}from"./CodeBlockWrapper.vue_vue_type_script_setup_true_lang-fwxGE1cB.js";import{I as P}from"./default-D33fL82q.js";import{u as V,f as j}from"./context-DeGNyDBn.js";import"../modules/shiki-BTcg5RPJ.js";const z=y({__name:"Transform",props:{scale:{},origin:{}},setup(d){const e=d,i=A(()=>{const t=[];return e.scale!=null&&t.push(`scale(${e.scale||1})`),{transform:t.join(" "),"transform-origin":e.origin||"top left"}});return(t,a)=>(r(),g("div",{style:B(i.value)},[D(t.$slots,"default")],4))}}),F={key:0,class:"w-30 h-30 my-10px bg-gray-400 bg-opacity-10 rounded-lg flex opacity-50"},I={class:"m-auto animate-pulse text-4xl"},W={key:0},q=y({__name:"Tweet",props:{id:{},scale:{},conversation:{},cards:{}},setup(d){const e=d,i=u(),t=u(!1),a=u(!1);async function p(n=10){var o,l;if(!((l=(o=window.twttr)==null?void 0:o.widgets)!=null&&l.createTweet)){if(n<=0)return console.error("Failed to load Twitter widget after 10 retries.");setTimeout(()=>p(n-1),1e3);return}const c=await window.twttr.widgets.createTweet(e.id.toString(),i.value,{theme:N.value?"dark":"light",conversation:e.conversation||"none",cards:e.cards});t.value=!0,c===void 0&&(a.value=!0)}return $(()=>{p()}),(n,c)=>{const o=S,l=z;return r(),v(l,{scale:n.scale||1},{default:m(()=>[s("div",{ref_key:"tweet",ref:i,class:"tweet slidev-tweet"},[!t.value||a.value?(r(),g("div",F,[s("div",I,[_(o),a.value?(r(),g("span",W,'Could not load tweet with id="'+x(e.id)+'"',1)):k("v-if",!0)])])):k("v-if",!0)],512)]),_:1},8,["scale"])}}}),L=s("h1",null,"The App’s Modularity",-1),R={grid:"~ cols-2 gap-4"},G=s("p",null,[h("Whenever a "),s("strong",null,"new models appears"),h(", adding its just about adding it in the config:")],-1),H=s("pre",{class:"shiki shiki-themes vitesse-dark vitesse-light slidev-code",style:{"--shiki-dark":"#dbd7caee","--shiki-light":"#393a34","--shiki-dark-bg":"#121212","--shiki-light-bg":"#ffffff"}},[s("code",{class:"language-py"},[s("span",{class:"line"},[s("span",{style:{"--shiki-dark":"#DBD7CAEE","--shiki-light":"#393A34"}},"model "),s("span",{style:{"--shiki-dark":"#666666","--shiki-light":"#999999"}},"="),s("span",{style:{"--shiki-dark":"#DBD7CAEE","--shiki-light":"#393A34"}}," st"),s("span",{style:{"--shiki-dark":"#666666","--shiki-light":"#999999"}},"."),s("span",{style:{"--shiki-dark":"#DBD7CAEE","--shiki-light":"#393A34"}},"selectbox"),s("span",{style:{"--shiki-dark":"#666666","--shiki-light":"#999999"}},"(")]),h(`
`),s("span",{class:"line"},[s("span",{style:{"--shiki-dark":"#C98A7D99","--shiki-light":"#B5695999"}},'    "'),s("span",{style:{"--shiki-dark":"#C98A7D","--shiki-light":"#B56959"}},"Select Model"),s("span",{style:{"--shiki-dark":"#C98A7D99","--shiki-light":"#B5695999"}},'"'),s("span",{style:{"--shiki-dark":"#666666","--shiki-light":"#999999"}},","),s("span",{style:{"--shiki-dark":"#DBD7CAEE","--shiki-light":"#393A34"}}," ")]),h(`
`),s("span",{class:"line"},[s("span",{style:{"--shiki-dark":"#666666","--shiki-light":"#999999"}},"    ("),s("span",{style:{"--shiki-dark":"#C98A7D99","--shiki-light":"#B5695999"}},'"'),s("span",{style:{"--shiki-dark":"#C98A7D","--shiki-light":"#B56959"}},"claude-3.5-sonnet-20240620"),s("span",{style:{"--shiki-dark":"#C98A7D99","--shiki-light":"#B5695999"}},'"'),s("span",{style:{"--shiki-dark":"#666666","--shiki-light":"#999999"}},","),s("span",{style:{"--shiki-dark":"#C98A7D99","--shiki-light":"#B5695999"}},'"'),s("span",{style:{"--shiki-dark":"#C98A7D","--shiki-light":"#B56959"}},"claude-3-opus-20240229"),s("span",{style:{"--shiki-dark":"#C98A7D99","--shiki-light":"#B5695999"}},'"'),s("span",{style:{"--shiki-dark":"#666666","--shiki-light":"#999999"}},","),s("span",{style:{"--shiki-dark":"#C98A7D99","--shiki-light":"#B5695999"}},' "'),s("span",{style:{"--shiki-dark":"#C98A7D","--shiki-light":"#B56959"}},"claude-3-sonnet-20240229"),s("span",{style:{"--shiki-dark":"#C98A7D99","--shiki-light":"#B5695999"}},'"'),s("span",{style:{"--shiki-dark":"#666666","--shiki-light":"#999999"}},")")]),h(`
`),s("span",{class:"line"},[s("span",{style:{"--shiki-dark":"#666666","--shiki-light":"#999999"}},")")])])],-1),J=s("p",null,"And that’s it, the app now allows to use the latest Anthropic Model",-1),K=s("p",null,"And we had very recent anouncements…",-1),es={__name:"9",setup(d){const{$slidev:e,$nav:i,$clicksContext:t,$clicks:a,$page:p,$renderContext:n,$frontmatter:c}=V();return(o,l)=>{const w=M,C=q;return r(),v(P,T(E(f(j)(f(c),8))),{default:m(()=>[L,s("div",R,[s("div",null,[G,_(w,b({},{ranges:[]}),{default:m(()=>[H]),_:1},16),J,k(" ./components/Counter.vue "),k(` <Counter :count="10" m="t-4" />

Check out [the guides](https://sli.dev/builtin/components.html) for more. `)]),s("div",null,[K,_(C,{id:"1803790676988920098",scale:"0.45"})])])]),_:1},16)}}};export{es as default};