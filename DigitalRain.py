from random import random
from time import sleep,time
from os import get_terminal_size
from sys import exit as Exit,stdout,argv

def randINT(max):
	return int(random()*(max))

def capmax(Num,Max):
	if 0<Num and Num<Max:return Num
	elif Num>Max:return Max
	else:return 0

#Unfortunately, all hirigana and kanji are full-width only. For now, all we have is katakana.
Languages={
	'e':('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'),

	'E':('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'),

	'#':('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'),

	'S':('!','#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', '{', '|', '}', '~','-', '‖', '‗','†', '‡', '•', '‣', '․', '‥', '…', '‧', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_','‰', '‱', '‹', '›', '※', '‼', '‽', '‾', '⁁', '⁂', '⁃', '⁄', '⁅', '⁆', '⁇', '⁈', '⁉'),

	'G':('Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω'),

	'g':('α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'ς', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω'),

	'H':('צּ', 'קּ', 'רּ', 'שּ', 'תּ', 'וֹ', 'בֿ', 'כֿ', 'פֿ', 'ﭏ', 'ףּ', 'פּ', 'שׁ', 'שׂ', 'שּׁ', 'שּׂ', 'אַ', 'אָ', 'אּ', 'בּ', 'גּ', 'דּ', 'הּ', 'וּ', 'זּ', 'נּ', 'סּ', 'מּ', 'טּ', 'יּ', 'ךּ', 'כּ', 'לּ', 'א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'ך', 'כ', 'ל', 'ם', 'מ', 'ן', 'נ', 'ס', 'ע', 'ף', 'פ', 'ץ', 'צ', 'ק', 'ר', 'ש', 'ת'),

	'o':('ሀ', 'ሁ', 'ሂ', 'ሃ', 'ሄ', 'ህ', 'ሆ', 'ሇ', 'ለ', 'ሉ', 'ሊ', 'ላ', 'ሌ', 'ል', 'ሎ', 'ሏ', 'ሐ', 'ሑ', 'ሒ', 'ሓ', 'ሔ', 'ሕ', 'ሖ', 'ሗ', 'መ', 'ሙ', 'ሚ', 'ማ', 'ሜ', 'ም', 'ሞ', 'ሟ', 'ሠ', 'ሡ', 'ሢ', 'ሣ', 'ሤ', 'ሥ', 'ሦ', 'ሧ', 'ረ', 'ሩ', 'ሪ', 'ራ', 'ሬ', 'ር', 'ሮ', 'ሯ', 'ሰ', 'ሱ', 'ሲ', 'ሳ', 'ሴ', 'ስ', 'ሶ', 'ሷ', 'ሸ', 'ሹ', 'ሺ', 'ሻ', 'ሼ', 'ሽ', 'ሾ', 'ሿ', 'ቀ', 'ቁ', 'ቂ', 'ቃ', 'ቄ', 'ቅ', 'ቆ', 'ቇ', 'ቈ', 'ዂ', 'ዃ', 'ዄ', 'ዅ', 'ጘ', 'ጙ', 'ጚ', 'ጛ', 'ጜ', 'ጝ', 'ጞ', 'ጟ', 'ጠ', 'ጡ', 'ጢ', 'ጣ', 'ጤ', 'ጥ', 'ጦ', 'ጧ', 'ጨ', 'ጩ', 'ጪ', 'ጫ', 'ጬ', 'ጭ', 'ጮ', 'ጯ', 'ጰ', 'ጱ', 'ጲ', 'ጳ', 'ጴ', 'ጵ', 'ጶ', 'ጷ', 'ጸ', 'ጹ', 'ጺ', 'ጻ', 'ጼ', 'ጽ', 'ጾ', 'ጿ', 'ፀ', 'ፁ', 'ፂ', 'ፃ', 'ፄ', 'ፅ', 'ፆ', 'ፇ', 'ፈ', 'ፉ', 'ፊ', 'ፋ', 'ፌ', 'ፍ', 'ፎ', 'ፏ', 'ፐ', 'ፑ', 'ፒ', 'ፓ', 'ፔ', 'ፕ', 'ፖ', 'ፗ', 'ፘ', 'ፙ', 'ፚ', 'ዀ', 'ነ', 'ኑ', 'ኒ', 'ና', 'ኔ', 'ን', 'ኖ', 'ኗ', 'ኘ', 'ኙ', 'ኚ', 'ኛ', 'ኜ', 'ኝ', 'ኞ', 'ኟ', 'አ', 'ኡ', 'ኢ', 'ኣ', 'ኤ', 'እ', 'ኦ', 'ኧ', 'ከ', 'ኩ', 'ኪ', 'ካ', 'ኬ', 'ክ', 'ኮ', 'ኯ', 'ኰ', 'ቐ', 'ቑ', 'ቒ', 'ቓ', 'ቔ', 'ቕ', 'ቖ', 'ኲ', 'ኳ', 'ኴ', 'ኵ', 'ወ', 'ዉ', 'ዊ', 'ዋ', 'ዌ', 'ው', 'ዎ', 'ዏ', 'ዐ', 'ዑ', 'ዒ', 'ዓ', 'ዔ', 'ዕ', 'ዖ', 'ኸ', 'ኹ', 'ኺ', 'ኻ', 'ኼ', 'ኽ', 'ኾ', 'ኊ', 'ኋ', 'ኌ', 'ኍ', 'ቚ', 'ቛ', 'ቜ', 'ቝ', 'ቊ', 'ቋ', 'ቌ', 'ቍ', 'ዘ', 'ዙ', 'ዚ', 'ዛ', 'ዜ', 'ዝ', 'ዞ', 'ዟ', 'ዠ', 'ዡ', 'ዢ', 'ዣ', 'ዤ', 'ዥ', 'ዦ', 'ዧ', 'የ', 'ዩ', 'ዪ', 'ያ', 'ዬ', 'ይ', 'ዮ', 'ዯ', 'ደ', 'ዱ', 'ዲ', 'ዳ', 'ዴ', 'ድ', 'ዶ', 'ዷ', 'ዸ', 'ዹ', 'ዺ', 'ዻ', 'ዼ', 'ዽ', 'ዾ', 'ዿ', 'ጀ', 'ጁ', 'ጂ', 'ጃ', 'ጄ', 'ጅ', 'ጆ', 'ጇ', 'ገ', 'ጉ', 'ጊ', 'ጋ', 'ጌ', 'ግ', 'ጎ', 'ጏ', 'ጐ', 'ቘ', 'ጒ', 'ጓ', 'ጔ', 'ጕ', 'በ', 'ቡ', 'ቢ', 'ባ', 'ቤ', 'ብ', 'ቦ', 'ቧ', 'ቨ', 'ቩ', 'ቪ', 'ቫ', 'ቬ', 'ቭ', 'ቮ', 'ቯ', 'ተ', 'ቱ', 'ቲ', 'ታ', 'ቴ', 'ት', 'ቶ', 'ቷ', 'ቸ', 'ቹ', 'ቺ', 'ቻ', 'ቼ', 'ች', 'ቾ', 'ቿ', 'ኀ', 'ኁ', 'ኂ', 'ኃ', 'ኄ', 'ኅ', 'ኆ', 'ኇ', 'ኈ'),

	'C':('ᐁ', 'ᐂ', 'ᐃ', 'ᐄ', 'ᐅ', 'ᐆ', 'ᐇ', 'ᐈ', 'ᐉ', 'ᐊ', 'ᐋ', 'ᐌ', 'ᐍ', 'ᐎ', 'ᐏ', 'ᐐ', 'ᐑ', 'ᐒ', 'ᐓ', 'ᐔ', 'ᐕ', 'ᐖ', 'ᐗ', 'ᐘ', 'ᐙ', 'ᐚ', 'ᐛ', 'ᐜ', 'ᐝ', 'ᐞ', 'ᐟ', 'ᐠ', 'ᐡ', 'ᐢ', 'ᐣ', 'ᐤ', 'ᐥ', 'ᐦ', 'ᐧ', 'ᐨ', 'ᐩ', 'ᐪ', 'ᐫ', 'ᐬ', 'ᐭ', 'ᐮ', 'ᐯ', 'ᐰ', 'ᐱ', 'ᐲ', 'ᐳ', 'ᐴ', 'ᐵ', 'ᐶ', 'ᐷ', 'ᐸ', 'ᐹ', 'ᐺ', 'ᐻ', 'ᐼ', 'ᐽ', 'ᐾ', 'ᐿ', 'ᑀ', 'ᑁ', 'ᑂ', 'ᑃ', 'ᑄ', 'ᑅ', 'ᑆ', 'ᑇ', 'ᑈ', 'ᑉ', 'ᑊ', 'ᑋ', 'ᑌ', 'ᑍ', 'ᑎ', 'ᑏ', 'ᑐ', 'ᑑ', 'ᑒ', 'ᑓ', 'ᑔ', 'ᑕ', 'ᑖ', 'ᑗ', 'ᑘ', 'ᑙ', 'ᑚ', 'ᑛ', 'ᑜ', 'ᑝ', 'ᑞ', 'ᑟ', 'ᑠ', 'ᑡ', 'ᑢ', 'ᑣ', 'ᑤ', 'ᑥ', 'ᑦ', 'ᑧ', 'ᑨ', 'ᑩ', 'ᑪ', 'ᑫ', 'ᑬ', 'ᑭ', 'ᑮ', 'ᑯ', 'ᑰ', 'ᑱ', 'ᑲ', 'ᑳ', 'ᑴ', 'ᑵ', 'ᑶ', 'ᑷ', 'ᑸ', 'ᑹ', 'ᑺ', 'ᑻ', 'ᑼ', 'ᑽ', 'ᑾ', 'ᑿ', 'ᒀ', 'ᒁ', 'ᒂ', 'ᒃ', 'ᒄ', 'ᒅ', 'ᒆ', 'ᒇ', 'ᒈ', 'ᒉ', 'ᒊ', 'ᒋ', 'ᒌ', 'ᒍ', 'ᒎ', 'ᒏ', 'ᒐ', 'ᒑ', 'ᒒ', 'ᒓ', 'ᒔ', 'ᒕ', 'ᒖ', 'ᒗ', 'ᒘ', 'ᒙ', 'ᒚ', 'ᒛ', 'ᒜ', 'ᒝ', 'ᒞ', 'ᒟ', 'ᒠ', 'ᒡ', 'ᒢ', 'ᒣ', 'ᒤ', 'ᒥ', 'ᒦ', 'ᒧ', 'ᒨ', 'ᒩ', 'ᒪ', 'ᒫ', 'ᒬ', 'ᒭ', 'ᒮ', 'ᒯ', 'ᒰ', 'ᒱ', 'ᒲ', 'ᒳ', 'ᒴ', 'ᒵ', 'ᒶ', 'ᒷ', 'ᒸ', 'ᒹ', 'ᒺ', 'ᒻ', 'ᒼ', 'ᒽ', 'ᒾ', 'ᒿ', 'ᓀ', 'ᓁ', 'ᓂ', 'ᓃ', 'ᓄ', 'ᓅ', 'ᓆ', 'ᓇ', 'ᓈ', 'ᓉ', 'ᓊ', 'ᓋ', 'ᓌ', 'ᓍ', 'ᓎ', 'ᓏ', 'ᓐ', 'ᓑ', 'ᓒ', 'ᓓ', 'ᓔ', 'ᓕ', 'ᓖ', 'ᓗ', 'ᓘ', 'ᓙ', 'ᓚ', 'ᓛ', 'ᓜ', 'ᓝ', 'ᓞ', 'ᓟ', 'ᓠ', 'ᓡ', 'ᓢ', 'ᓣ', 'ᓤ', 'ᓥ', 'ᓦ', 'ᓧ', 'ᓨ', 'ᓩ', 'ᓪ', 'ᓫ', 'ᓬ', 'ᓭ', 'ᓮ', 'ᓯ', 'ᓰ', 'ᓱ', 'ᓲ', 'ᓳ', 'ᓴ', 'ᓵ', 'ᓶ', 'ᓷ', 'ᓸ', 'ᓹ', 'ᓺ', 'ᓻ', 'ᓼ', 'ᓽ', 'ᓾ', 'ᓿ', 'ᔀ', 'ᔁ', 'ᔂ', 'ᔃ', 'ᔄ', 'ᔅ', 'ᔆ', 'ᔇ', 'ᔈ', 'ᔉ', 'ᔊ', 'ᔋ', 'ᔌ', 'ᔍ', 'ᔎ', 'ᔏ', 'ᔐ', 'ᔑ', 'ᔒ', 'ᔓ', 'ᔔ', 'ᔕ', 'ᔖ', 'ᔗ', 'ᔘ', 'ᔙ', 'ᔚ', 'ᔛ', 'ᔜ', 'ᔝ', 'ᔞ', 'ᔟ', 'ᔠ', 'ᔡ', 'ᔢ', 'ᔣ', 'ᔤ', 'ᔥ', 'ᔦ', 'ᔧ', 'ᔨ', 'ᔩ', 'ᔪ', 'ᔫ', 'ᔬ', 'ᔭ', 'ᔮ', 'ᔯ', 'ᔰ', 'ᔱ', 'ᔲ', 'ᔳ', 'ᔴ', 'ᔵ', 'ᔶ', 'ᔷ', 'ᔸ', 'ᔹ', 'ᔺ', 'ᔻ', 'ᔼ', 'ᔽ', 'ᔾ', 'ᔿ', 'ᕀ', 'ᕁ', 'ᕂ', 'ᕃ', 'ᕄ', 'ᕅ', 'ᕆ', 'ᕇ', 'ᕈ', 'ᕉ', 'ᕊ', 'ᕋ', 'ᕌ', 'ᕍ', 'ᕎ', 'ᕏ', 'ᕐ', 'ᕑ', 'ᕒ', 'ᕓ', 'ᕔ', 'ᕕ', 'ᕖ', 'ᕗ', 'ᕘ', 'ᕙ', 'ᕚ', 'ᕛ', 'ᕜ', 'ᕝ', 'ᕞ', 'ᕟ', 'ᕠ', 'ᕡ', 'ᕢ', 'ᕣ', 'ᕤ', 'ᕥ', 'ᕦ', 'ᕧ', 'ᕨ', 'ᕩ', 'ᕪ', 'ᕫ', 'ᕬ', 'ᕭ', 'ᕮ', 'ᕯ', 'ᕰ', 'ᕱ', 'ᕲ', 'ᕳ', 'ᕴ', 'ᕵ', 'ᕶ', 'ᕷ', 'ᕸ', 'ᕹ', 'ᕺ', 'ᕻ', 'ᕼ', 'ᕽ', 'ᕾ', 'ᕿ', 'ᖀ', 'ᖁ', 'ᖂ', 'ᖃ', 'ᖄ', 'ᖅ', 'ᖆ', 'ᖇ', 'ᖈ', 'ᖉ', 'ᖊ', 'ᖋ', 'ᖌ', 'ᖍ', 'ᖎ', 'ᖏ', 'ᖐ', 'ᖑ', 'ᖒ', 'ᖓ', 'ᖔ', 'ᖕ', 'ᖖ', 'ᖗ', 'ᖘ', 'ᖙ', 'ᖚ', 'ᖛ', 'ᖜ', 'ᖝ', 'ᖞ', 'ᖟ', 'ᖠ', 'ᖡ', 'ᖢ', 'ᖣ', 'ᖤ', 'ᖥ', 'ᖦ', 'ᖧ', 'ᖨ', 'ᖩ', 'ᖪ', 'ᖫ', 'ᖬ', 'ᖭ', 'ᖮ', 'ᖯ', 'ᖰ', 'ᖱ', 'ᖲ', 'ᖳ', 'ᖴ', 'ᖵ', 'ᖶ', 'ᖷ', 'ᖸ', 'ᖹ', 'ᖺ', 'ᖻ', 'ᖼ', 'ᖽ', 'ᖾ', 'ᖿ', 'ᗀ', 'ᗁ', 'ᗂ', 'ᗃ', 'ᗄ', 'ᗅ', 'ᗆ', 'ᗇ', 'ᗈ', 'ᗉ', 'ᗊ', 'ᗋ', 'ᗌ', 'ᗍ', 'ᗎ', 'ᗏ', 'ᗐ', 'ᗑ', 'ᗒ', 'ᗓ', 'ᗔ', 'ᗕ', 'ᗖ', 'ᗗ', 'ᗘ', 'ᗙ', 'ᗚ', 'ᗛ', 'ᗜ', 'ᗝ', 'ᗞ', 'ᗟ', 'ᗠ', 'ᗡ', 'ᗢ', 'ᗣ', 'ᗤ', 'ᗥ', 'ᗦ', 'ᗧ', 'ᗨ', 'ᗩ', 'ᗪ', 'ᗫ', 'ᗬ', 'ᗭ', 'ᗮ', 'ᗯ', 'ᗰ', 'ᗱ', 'ᗲ', 'ᗳ', 'ᗴ', 'ᗵ', 'ᗶ', 'ᗷ', 'ᗸ', 'ᗹ', 'ᗺ', 'ᗻ', 'ᗼ', 'ᗽ', 'ᗾ', 'ᗿ', 'ᘀ', 'ᘁ', 'ᘂ', 'ᘃ', 'ᘄ', 'ᘅ', 'ᘆ', 'ᘇ', 'ᘈ', 'ᘉ', 'ᘊ', 'ᘋ', 'ᘌ', 'ᘍ', 'ᘎ', 'ᘏ', 'ᘐ', 'ᘑ', 'ᘒ', 'ᘓ', 'ᘔ', 'ᘕ', 'ᘖ', 'ᘗ', 'ᘘ', 'ᘙ', 'ᘚ', 'ᘛ', 'ᘜ', 'ᘝ', 'ᘞ', 'ᘟ', 'ᘠ', 'ᘡ', 'ᘢ', 'ᘣ', 'ᘤ', 'ᘥ', 'ᘦ', 'ᘧ', 'ᘨ', 'ᘩ', 'ᘪ', 'ᘫ', 'ᘬ', 'ᘭ', 'ᘮ', 'ᘯ', 'ᘰ', 'ᘱ', 'ᘲ', 'ᘳ', 'ᘴ', 'ᘵ', 'ᘶ', 'ᘷ', 'ᘸ', 'ᘹ', 'ᘺ', 'ᘻ', 'ᘼ', 'ᘽ', 'ᘾ', 'ᘿ', 'ᙀ', 'ᙁ', 'ᙂ', 'ᙃ', 'ᙄ', 'ᙅ', 'ᙆ', 'ᙇ', 'ᙈ', 'ᙉ', 'ᙊ', 'ᙋ', 'ᙌ', 'ᙍ', 'ᙎ', 'ᙏ', 'ᙐ', 'ᙑ', 'ᙒ', 'ᙓ', 'ᙔ', 'ᙕ', 'ᙖ', 'ᙗ', 'ᙘ', 'ᙙ', 'ᙚ', 'ᙛ', 'ᙜ', 'ᙝ', 'ᙞ', 'ᙟ', 'ᙠ', 'ᙡ', 'ᙢ', 'ᙣ', 'ᙤ', 'ᙥ', 'ᙦ', 'ᙧ', 'ᙨ', 'ᙩ', 'ᙪ', 'ᙫ', 'ᙬ', '᙭', '᙮', 'ᙯ', 'ᙰ', 'ᙱ', 'ᙲ', 'ᙳ', 'ᙴ', 'ᙵ', 'ᙶ'),

	'R':('ᚠ', 'ᚡ', 'ᚢ', 'ᚣ', 'ᚤ', 'ᚥ', 'ᚦ', 'ᚧ', 'ᚨ', 'ᚩ', 'ᚪ', 'ᚫ', 'ᚬ', 'ᚭ', 'ᚮ', 'ᚯ', 'ᚰ', 'ᚱ', 'ᚲ', 'ᚳ', 'ᚴ', 'ᚵ', 'ᚶ', 'ᚷ', 'ᚸ', 'ᚹ', 'ᚺ', 'ᚻ', 'ᚼ', 'ᚽ', 'ᚾ', 'ᚿ', 'ᛀ', 'ᛁ', 'ᛂ', 'ᛃ', 'ᛄ', 'ᛅ', 'ᛆ', 'ᛇ', 'ᛈ', 'ᛉ', 'ᛊ', 'ᛋ', 'ᛌ', 'ᛍ', 'ᛎ', 'ᛏ', 'ᛐ', 'ᛑ', 'ᛒ', 'ᛓ', 'ᛔ', 'ᛕ', 'ᛖ', 'ᛗ', 'ᛘ', 'ᛙ', 'ᛚ', 'ᛛ', 'ᛜ', 'ᛝ', 'ᛞ', 'ᛟ', 'ᛠ', 'ᛡ', 'ᛢ', 'ᛣ', 'ᛤ', 'ᛥ', 'ᛦ', 'ᛧ', 'ᛨ', 'ᛩ', 'ᛪ', '᛫', '᛬', '᛭', 'ᛮ', 'ᛯ', 'ᛰ'),

	'K':('｡', '｢', '｣', '､', '･', 'ｦ', 'ｧ', 'ｨ', 'ｩ', 'ｪ', 'ｫ', 'ｬ', 'ｭ', 'ｮ', 'ｯ', 'ｰ', 'ｱ', 'ｲ', 'ｳ', 'ｴ', 'ｵ', 'ｶ', 'ｷ', 'ｸ', 'ｹ', 'ｺ', 'ｻ', 'ｼ', 'ｽ', 'ｾ', 'ｿ', 'ﾀ', 'ﾁ', 'ﾂ', 'ﾃ', 'ﾄ', 'ﾅ', 'ﾆ', 'ﾇ', 'ﾈ', 'ﾉ', 'ﾊ', 'ﾋ', 'ﾌ', 'ﾍ', 'ﾎ', 'ﾏ', 'ﾐ', 'ﾑ', 'ﾒ', 'ﾓ', 'ﾔ', 'ﾕ', 'ﾖ', 'ﾗ', 'ﾘ', 'ﾙ', 'ﾚ', 'ﾛ', 'ﾜ', 'ﾝ', 'ﾞ', 'ﾟ'),

	'r':('₠', '₡', '₢', '₣', '₤', '₥', '₦', '₧', '₨', '₩', '₪', '₫', '€', '₭', '₮', '₯'),

	'B':('⠁', '⠂', '⠃', '⠄', '⠅', '⠆', '⠇', '⠈', '⠉', '⠊', '⠋', '⠌', '⠍', '⠎', '⠏', '⠐', '⠑', '⠒', '⠓', '⠔', '⠕', '⠖', '⠗', '⠘', '⠙', '⠚', '⠛', '⠜', '⠝', '⠞', '⠟', '⠠', '⠡', '⠢', '⠣', '⠤', '⠥', '⠦', '⠧', '⠨', '⠩', '⠪', '⠫', '⠬', '⠭', '⠮', '⠯', '⠰', '⠱', '⠲', '⠳', '⠴', '⠵', '⠶', '⠷', '⠸', '⠹', '⠺', '⠻', '⠼', '⠽', '⠾', '⠿', '⡀', '⡁', '⡂', '⡃', '⡄', '⡅', '⡆', '⡇', '⡈', '⡉', '⡊', '⡋', '⡌', '⡍', '⡎', '⡏', '⡐', '⡑', '⡒', '⡓', '⡔', '⡕', '⡖', '⡗', '⡘', '⡙', '⡚', '⡛', '⡜', '⡝', '⡞', '⡟', '⡠', '⡡', '⡢', '⡣', '⡤', '⡥', '⡦', '⡧', '⡨', '⡩', '⡪', '⡫', '⡬', '⡭', '⡮', '⡯', '⡰', '⡱', '⡲', '⡳', '⡴', '⡵', '⡶', '⡷', '⡸', '⡹', '⡺', '⡻', '⡼', '⡽', '⡾', '⡿', '⢀', '⢁', '⢂', '⢃', '⢄', '⢅', '⢆', '⢇', '⢈', '⢉', '⢊', '⢋', '⢌', '⢍', '⢎', '⢏', '⢐', '⢑', '⢒', '⢓', '⢔', '⢕', '⢖', '⢗', '⢘', '⢙', '⢚', '⢛', '⢜', '⢝', '⢞', '⢟', '⢠', '⢡', '⢢', '⢣', '⢤', '⢥', '⢦', '⢧', '⢨', '⢩', '⢪', '⢫', '⢬', '⢭', '⢮', '⢯', '⢰', '⢱', '⢲', '⢳', '⢴', '⢵', '⢶', '⢷', '⢸', '⢹', '⢺', '⢻', '⢼', '⢽', '⢾', '⢿', '⣀', '⣁', '⣂', '⣃', '⣄', '⣅', '⣆', '⣇', '⣈', '⣉', '⣊', '⣋', '⣌', '⣍', '⣎', '⣏', '⣐', '⣑', '⣒', '⣓', '⣔', '⣕', '⣖', '⣗', '⣘', '⣙', '⣚', '⣛', '⣜', '⣝', '⣞', '⣟', '⣠', '⣡', '⣢', '⣣', '⣤', '⣥', '⣦', '⣧', '⣨', '⣩', '⣪', '⣫', '⣬', '⣭', '⣮', '⣯', '⣰', '⣱', '⣲', '⣳', '⣴', '⣵', '⣶', '⣷', '⣸', '⣹', '⣺', '⣻', '⣼', '⣽', '⣾', '⣿'),

	'n':('Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ', 'Ⅶ', 'Ⅷ', 'Ⅸ', 'Ⅹ', 'Ⅺ', 'Ⅻ', 'Ⅼ', 'Ⅽ', 'Ⅾ', 'Ⅿ', 'ⅰ', 'ⅱ', 'ⅲ', 'ⅳ', 'ⅴ', 'ⅵ', 'ⅶ', 'ⅷ', 'ⅸ', 'ⅹ', 'ⅺ', 'ⅻ', 'ⅼ', 'ⅽ', 'ⅾ', 'ⅿ', 'ↀ'),

	'b':('0','1')
	#On some terminals, ANSI colours can't affect non-english characters.
	#On some terminals, all the characters deteriorate into CJK. (WTF)
	#I would move this all to a file, but for it to be any more readable, it would need to store it without the whole escape code thing.
}
ArgDict=dict()
for i in argv[1:]:
	try:
		ArgDict[CurrentArg].append(int(i))
	except:
		if '-' in i:
			ArgDict[i.replace('-','').lower()[0]]=list()
			CurrentArg=i.replace('-','').lower()[0]
		else:
			ArgDict[CurrentArg].append(i)#Gotta be a better way to do that whole "negative indexing" thing.

for i in ArgDict:
	if len(ArgDict[i])==1:#There's probably some way to reference it without [i] every time.
		ArgDict[i]=ArgDict[i][0]

if 'h' in ArgDict.keys() or '?' in ArgDict.keys():
	Exit(
"""-h\t--help\t\tDisplay this help screen.
-s\t--speed\t\tThe target amount of time a cycle takes, as a fraction of a second. (Default is .15)
-t\t--trail-length\tTrail length, as a fraction of the screen. (Default is 1/2)
-f\t--fluctuation\tFluctuation in the colour of the trail. (Default is 20)
-a\t--amount\tNumber of droplets coming down the screen. Can be a fraction or integer. (Default is 1/2)
-r\t--refill\tWhen resizing the window, fill the space with extra droplets. (Default true, this turn it off.)
-l\t--language\tLetters that can fall. Add the letters, seperated by spaces, to this argument to add them. (Case sensitive)
\t(K)atakana
\t(E)nglish - Uppercase
\t(e)nglish - lowercase
\t(G)reek - Uppercase
\t(g)reek - lowercase
\t(#) - Numbers
\t(H)ebrew
\t(R)unic
\t(C)anadian syllabics
\tEthi(o)pic
\t(B)raille
\t(b)inary
\tRoman (n)umerals
\tCu(r)rencies
-c\t--colour\tChanges the colour of the trails.
\t0: (R)ed
\t1: (G)reen
\t2: (B)lue
\t3: Gr(A)y
\t4: (RGB)
\t5: (RGBA)
""")
	
#It seems like I'm going to have to make my own argv module. That will come later.

def ArgFraction(Index):
	try:Var=float(ArgDict[Index])
	except ValueError:
		SlashLoc=ArgDict[Index].find('/')
		Var=int(ArgDict[Index][:SlashLoc])  /  int(ArgDict[Index][SlashLoc+1:])
	except KeyError:Var=.5
	return 1/(Var)#Can be a float, it gets rounded later.

TrailFraction=ArgFraction('t')
FreqMult=ArgFraction('a')
try:Speed=float(ArgDict['s'])
except ValueError:
		SlashLoc=ArgDict['s'].find('/')
		Speed=int(ArgDict['s'][:SlashLoc])  /  int(ArgDict['s'][SlashLoc+1:])
except KeyError:Speed=.15

try:Fluctuation=int(ArgDict['f'])
except KeyError:Fluctuation=20

ColourModes=('R','G','B','A','RGB','RGBA')
try:
	ColourMode=int(ArgDict['c'])
	ColourMode=capmax(ColourMode,6)
except ValueError:
	ColourMode=ArgDict['c'].upper()
	try:ColourMode=ColourModes.index(ColourMode)
	except ValueError:ColourMode=1
except KeyError:ColourMode=1

Letters=list()
if 'l' in ArgDict.keys():
	for i in ArgDict['l']:
		if i in Languages.keys():
			Letters.extend(Languages[i])
else:
	Letters.extend(Languages['E'])
	Letters.extend(Languages['G'])	
	Letters.extend(Languages['g'])
del Languages

WindSheild=list(get_terminal_size())
WindSheild[1]-=1
Matrix=[[0]*WindSheild[0]]*WindSheild[1]

TrailLength=int(WindSheild[1]/TrailFraction)
ColourCap=int(255/TrailLength)
Frequency=int(WindSheild[1]*FreqMult)

def ChangeTrail(Gloss):
	global TrailLength
	global ColourCap
	NewTrailLength=int(Gloss[1]/TrailFraction)
	for i in range(Gloss[1]):
		for g in range(Gloss[0]):
			if Matrix[i][g]!=0:
				if Matrix[i][g][0]==TrailLength:
					Matrix[i][g][0]=NewTrailLength
	TrailLength=NewTrailLength
	ColourCap=int(255/TrailLength)

def ResizeWindsheild(WindSheild):
	Glass=list(get_terminal_size())
	Glass[1]-=1

	if WindSheild[0]>Glass[0]:
		for i in range(WindSheild[1]):
			del Matrix[i][-(WindSheild[0]-Glass[0]):]
	elif WindSheild[0]<Glass[0]:
		for i in range(WindSheild[1]):
			Matrix[i].extend([0]*(Glass[0]-WindSheild[0]))
			if not 'R' in ArgDict.keys():
				for Refill in range(WindSheild[0],Glass[0]):
					if randINT(Frequency)==0:
						if ColourMode<4:ItemCol=ColourMode
						elif ColourMode==4:ItemCol=randINT(3)
						else: ItemCol=randINT(4)
						Matrix[i][Refill]=[TrailLength,ItemCol]
						iPos=i
						for Streak in range(TrailLength-1,0,-1):
							iPos-=1
							try:Matrix[iPos][Refill]=[Streak,ItemCol]
							except IndexError:break

	if WindSheild[1]>Glass[1]:	
		del Matrix[-(WindSheild[1]-Glass[1]):]
		ChangeTrail(Glass)
	elif WindSheild[1]<Glass[1]:
		Matrix.extend([[0]*Glass[0]]*(Glass[1]-WindSheild[1]))
		ChangeTrail(Glass)

	WindSheild=Glass
	return WindSheild

def LetterThingy(Col):
		Fluc=randINT(Fluctuation) if random()<.5 else randINT(-Fluctuation)
		Intensity=capmax(Col[0]*ColourCap+Fluc,255)
		match Col[1]:
			case 0:return f'\x1b[38;2;{Intensity};0;0m{Letters[randINT(len(Letters))]}\x1b[0m'
			case 1:return f'\x1b[38;2;0;{Intensity};0m{Letters[randINT(len(Letters))]}\x1b[0m'
			case 2:return f'\x1b[38;2;0;0;{Intensity}m{Letters[randINT(len(Letters))]}\x1b[0m'
			case 3:return f'\x1b[38;2;{Intensity};{Intensity};{Intensity}m{Letters[randINT(len(Letters))]}\x1b[0m'

stdout.write('\x1b[?25l')
Buffer=list()
Append=Buffer.append
while True:
	StartLoop=time()
	try:
		if get_terminal_size()[0]!=WindSheild[0] or get_terminal_size()[1]-1!=WindSheild[1]:
			WindSheild=ResizeWindsheild(WindSheild)
		del Matrix[-1]
		Matrix.insert(0,[0]*WindSheild[0])
		for i in range(WindSheild[0]):
			if Matrix[1][i]!=0:
				if Matrix[1][i][0]!=0:
					Matrix[0][i]=[Matrix[1][i][0]-1,Matrix[1][i][1]]
		
		for i in range(WindSheild[0]):
			if randINT(Frequency)==0:
				if ColourMode<4:Matrix[0][i]=[TrailLength,ColourMode]
				elif ColourMode==4:Matrix[0][i]=[TrailLength,randINT(3)]
				else: Matrix[0][i]=[TrailLength,randINT(4)]
		for Row in Matrix:
			for Block in Row:
				if Block==0:Append(' ')
				elif Block[0]==TrailLength:Append(f'\x1b[1;38;2;255;255;255m{Letters[randINT(len(Letters))]}\x1b[0m')
				else:Append(LetterThingy(Block))
			Append('\n')
		Append('\x1b[0;0H')
		stdout.write(''.join(Buffer))
		del Buffer[:]
		try:sleep(Speed-(time()-StartLoop))
		except ValueError:continue
	except KeyboardInterrupt:
		Exit(f"\x1b[0m\x1b[?25h\x1b[{WindSheild[1]};0H")
