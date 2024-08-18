import ChatTTS
import torch
import soundfile
import cn2an
from playsound import playsound
import re
import textPreprocessing as tp

class Text2Speech:
    def __init__(self,random_seed=2,temperature=.3,top_P=0.7,top_K=20):
        self.random_seed = random_seed
        torch.manual_seed(self.random_seed)
        self.chat = ChatTTS.Chat()
        self.chat.load(compile=False) 
        ###################################
        # Sample a speaker from Gaussian.
        self.rand_spk = self.chat.sample_random_speaker()
        #print(rand_spk) # save it for later timbre recovery
        self.temperature = temperature
        self.top_P = top_P
        self.top_K = top_K

        self.params_infer_code = ChatTTS.Chat.InferCodeParams(
            spk_emb = self.rand_spk,#"蘁淰敝欀佄乊甁覻爞珠耣生呙浧爂燍盦笰媣咱眢捲悁让葐栐悘擭蚐瘜娽湶挪帒牬舫諷攵揩薿腟坙嶟嵜傹檺安癠嚬攍葓趝卒椎衺磻莱凥墯硶緝椡嬤喆氒叄侕畬曍溤涌棁诃玟螾堈禂疋泙洉咄揹蘟箱徹勉豣晠菼異婁誤堳勗滩殶瞃趿綸修諸沂愥篯朄瞡掅瀚涕扵蘧剼愅斌氪揶藽拷僗墏巾祫薪玐衫趶瞕慏罯簜淹圚絳谯苊絩毿橣悡荕蜷橕垐嚜嵖囪澂訟烢僴喊毕艋烖蔈禀植壜忴莩竨粧懄国繀涽厸勶茙底渨苓樫螤哜伶腊獫儕蟺嘲枮曋沤圆纙换槈熲渜磞襭潩嵂熌梟撚狣蚼蛪炨菑敋綹玒滿砭姽國觐嚸桖冼覚癶姱昿厙起峬容砯似賿堭囅蛲戓萝瑤壡匔娓婜衊愮凍翆渆涤瘬賅塶戳傩殤赭褕世礔佂勆缉凣蝭倚峁唍譛捂蚲蒻縜垚諫惏勑戼脕湣厦罯淙匜禅蒌桭繃浟创疍犖袯紥紮氪婁耕蓃哄朁繴粨瓆慼觴欭痮槪峮挪払廼螇圾蜇媈朸敠筣財溳晵譢傐秀咂灭憾单渋謧琬蝊觘肌謑嬰膰杮刅嶞呅袢字嫜您嵍槗潟尹囬穓岂枟槫嫧殭絯椪譱耰恲肵兵堲誽岞戠蓫匙灐唯覇硅趖旨蝝廘罸毶組唆檄敫昧篼禌敉覹圏哮素乵溅赅噇础剬戁濄葱夤丵偭侬儙祆楰縊孌盹緺擵婦存嗨窗苦莦艂紬司蜳币崁断繀蓨砞婖裸莕卽斱粘漏蛑宱豽朹帖睰凵溒皿坍訴负於嵢埖溃濷棑劁襔櫧孃搏偎猻臟簞怳肫椯乮爊眤亢枞皅谝椤政绮沓砍屋幗綋獜傒暜惘皚惻腻抈糽語芶喹潡蓢缬仅窒殞掿緀瀸旺炣姚氈搄禃徵櫩改獞溿衠袍叏尼稼誻察爕喝貝何狽栝琓洛藳瞝桱楗俟豓爷团噅態劽取萙蔱峴垁巋箽獙刮讜藑耹栘服渳蟅貍衘掌憼讛螄獷羒摯嬻燔悼乛妄熫灒养叒伬劚侅凒痢矨怅嬗瀽賰圅哎杉礚僌沃杍圃緁仴廰慘耟嶭椘刢墫濾树戼替觉揸貒蒉斷淦婥惧丞憏垷旪瘦蓖狡劫考艁欣氇謸蜾俓瀛繑蟂届趜蚶猱挠襘綬婿褑碉硳嶑勗強擊勰狠噳仴撋够贴禧售直祏材蘛楷看袷臅豥唳朆萅俴檍帥苰昊勉搜宑娼栍牠瑈祔瀁兴蟍敻被厛巿褮袸矌禶盚谹店榄偳詡倇婩怂穘楓股蝇趁樐巁椉濸缸兤蔏嵙癍覂簪喫擾祕枦瘈曒撅殁職萄槯妞蛾訌续楚抒藋侔埁薣礼见瘜埽嬵紊繧瀍冞夈筚簽孇犋乬桳孇藻堦淖舣海燍嫰淂嵣蚾滱荅仌性枰妾壛屃肘慱袢时瞠趓掺薬橱劔亪薺訤瘥勈熕縊层腙謯綬弑栏揀樨惾矗厳岾摭拾筵蘑滀怕罬巢砭笉抠戎綜塶琖塸譾纎栵秷砜燄萦嶁秋巣絵甋蓰繹川濆懝妊娖蒈灯熄怭掏衫凾睦娨綢蘶梢囇榴襇壢袻漛仪秽捺幜潹弗祮毭褝尳絵搑絃歫嘀㴅", # add sampled speaker 
            temperature = self.temperature,   # using custom temperature
            top_P = self.top_P,        # top P decode
            top_K = self.top_K,         # top K decode
        )
        ###################################
        # For sentence level manual control.

        # use oral_(0-9), laugh_(0-2), break_(0-7) 
        # to generate special token in text to synthesize.
        self.params_refine_text = ChatTTS.Chat.RefineTextParams(
            prompt='[oral_2][laugh_0][break_6]',
        )
    def text2speech(self,text,file_name):
        ###################################
        # For word level manual control.
        self.texts=[cn2an.transform(text,"an2cn")][0]
        print(self.texts)
        self.texts=re.sub(r'[\n\r\t]',"。",self.texts)
        # self.texts=tp.TextUtils(self.texts).convert_half_width_to_full_width()
        # print(self.texts)
        self.texts=str(self.texts).split("。")
        wavs=[]
        c=0
        for t in self.texts:
            wavs.append(self.chat.infer(t+"。", 
                                skip_refine_text=True, 
                                params_refine_text=self.params_refine_text,  
                                params_infer_code=self.params_infer_code,
                                refine_text_only=True))
            soundfile.write(file_name+str(c)+".wav",wavs[c][0], 22050)
            c+=1
        c=0
        for c in range(len(self.texts)):
            playsound(file_name+str(c)+".wav")
#测试
# t2s= Text2Speech()
# t2s.text2speech("引力透镜效应（Gravitational Lens Effect）是指一种在广义相对论中发挥的现象，通过引力来改变光线的传输方式。当一个大型物体（如星系、星球或者黑洞）在光线的路径上存在时，引力会导致光线的曲曲折折，并且会产生一个类似于镜头一样的效果。", "test")