# -*- coding: utf-8 -*-
# 14.11.2026: правки сайта под Prau 1.1.14.
#  • голос загружается прямо в Prau (Настройки → Языки → микрофон с плюсом),
#    старая инструкция про клавиатуру и «Языки диктовки» снята;
#  • карточка «Автоопределение языка» (глобус на главном экране);
#  • «Сделано надолго»: вместо застывшего «Version 1.1 is out now» — частые
#    обновления и что вышло после запуска;
#  • «Prau 1.0» в подписи к экранам убран.
# Применяется в build_site.py поверх strings_base / strings_new / strings_intl /
# strings_compare: исходные тексты не тронуты, откат — убрать импорт U.
#
# Ключи: see_sub, setup_sub, voice=(заголовок, текст) — 2-й пункт setup,
# tip — setup_tip, faq0 — ответ на 1-й вопрос поддержки (вопрос прежний),
# auto=(иконка, заголовок, текст) — новая карточка, next_ — строка в «Сделано надолго».
U = {}

U["en"] = dict(
 see_sub="Every screen below is Prau as it runs on an iPhone today.",
 setup_sub="Do it once at home on Wi-Fi — a few minutes in all. After that everything works with no network at all.",
 voice=("Voice input — downloaded right in Prau",
        "Prau downloads the speech model for each language itself — during the first setup, or later in Prau → Settings → Languages: tap the microphone with a plus next to a language. Nothing to change in iPhone Settings. A green microphone means the language is ready for voice."),
 tip="Text and photo translation don't need the voice model — they work as soon as the packs are in.",
 faq0="The voice model for that language isn't on your iPhone yet. Open Prau → Settings → Languages and tap the microphone next to the language — Prau downloads it, fastest on Wi-Fi. Until then, text and photo translation work fully.",
 auto=("🌐", "Automatic language detection",
       "Tap the globe on the main screen and stop switching sides: Prau hears which of your two languages is spoken and translates into the other. Two people simply talk in turn."),
 next_="Since launch in August, Prau has had more than a dozen updates: Stream subtitles, Siri and the Action Button, conversation summaries, automatic language detection. Every release also makes recognition and translation faster and more accurate — and the next features are already in the works.",
)

U["ru"] = dict(
 see_sub="Каждый экран ниже — Prau таким, каким он работает на iPhone сегодня.",
 setup_sub="Сделайте это один раз дома по Wi-Fi — всего несколько минут. Дальше всё работает вообще без сети.",
 voice=("Голосовой ввод — загрузка прямо в Prau",
        "Prau сам скачивает модель распознавания речи для каждого языка — при первой настройке или позже в Prau → Настройки → Языки: нажмите на микрофон с плюсом рядом с языком. В настройках iPhone ничего менять не нужно. Зелёный микрофон означает, что язык готов к голосу."),
 tip="Переводу текста и фото модель речи не нужна — он работает, как только скачаны пакеты.",
 faq0="Модели распознавания речи для этого языка на iPhone ещё нет. Откройте Prau → Настройки → Языки и нажмите на микрофон рядом с языком — Prau её скачает, быстрее всего по Wi-Fi. Пока она загружается, перевод текста и фото работает полностью.",
 auto=("🌐", "Автоопределение языка",
       "Нажмите на глобус на главном экране — и больше не переключайте направление: Prau сам слышит, на каком из двух языков говорят, и переводит на другой. Двое просто говорят по очереди."),
 next_="С запуска в августе у Prau вышло больше десятка обновлений: субтитры в режиме «Поток», Siri и кнопка действия, выжимка разговора, автоопределение языка. Каждый релиз ещё и делает распознавание и перевод быстрее и точнее — а следующие функции уже в работе.",
)

U["uk"] = dict(
 see_sub="Кожен екран нижче — Prau таким, яким він працює на iPhone сьогодні.",
 setup_sub="Зробіть це один раз удома по Wi-Fi — усього кілька хвилин. Далі все працює взагалі без мережі.",
 voice=("Голосове введення — завантаження просто в Prau",
        "Prau сам завантажує модель розпізнавання мовлення для кожної мови — під час першого налаштування або пізніше в Prau → Параметри → Мови: торкніться мікрофона з плюсом поруч із мовою. У налаштуваннях iPhone нічого змінювати не треба. Зелений мікрофон означає, що мова готова до голосу."),
 tip="Перекладу тексту й фото модель мовлення не потрібна — він працює, щойно завантажено пакети.",
 faq0="Моделі розпізнавання мовлення для цієї мови на iPhone ще немає. Відкрийте Prau → Параметри → Мови й торкніться мікрофона поруч із мовою — Prau її завантажить, найшвидше по Wi-Fi. Поки вона завантажується, переклад тексту й фото працює повністю.",
 auto=("🌐", "Автовизначення мови",
       "Торкніться глобуса на головному екрані — і більше не перемикайте напрямок: Prau сам чує, якою з двох мов говорять, і перекладає іншою. Двоє просто говорять по черзі."),
 next_="Від запуску в серпні Prau отримав понад десяток оновлень: субтитри в режимі «Потік», Siri та кнопку дії, стислий переказ розмови, автовизначення мови. Кожен реліз ще й робить розпізнавання та переклад швидшими й точнішими — а наступні функції вже в роботі.",
)

U["fr"] = dict(
 see_sub="Chaque écran ci-dessous est Prau tel qu'il tourne aujourd'hui sur iPhone.",
 setup_sub="À faire une fois chez vous en Wi-Fi — quelques minutes en tout. Ensuite tout fonctionne sans aucun réseau.",
 voice=("La saisie vocale — téléchargée directement dans Prau",
        "Prau télécharge lui-même le modèle de reconnaissance vocale de chaque langue — lors de la première configuration, ou plus tard dans Prau → Réglages → Langues : touchez le micro avec un plus à côté d'une langue. Rien à changer dans les Réglages de l'iPhone. Un micro vert signifie que la langue est prête pour la voix."),
 tip="La traduction de texte et de photos n'a pas besoin du modèle vocal — elle fonctionne dès que les packs sont installés.",
 faq0="Le modèle vocal de cette langue n'est pas encore sur votre iPhone. Ouvrez Prau → Réglages → Langues et touchez le micro à côté de la langue — Prau le télécharge, plus vite en Wi-Fi. En attendant, la traduction de texte et de photos fonctionne pleinement.",
 auto=("🌐", "Détection automatique de la langue",
       "Touchez le globe sur l'écran principal et n'inversez plus le sens : Prau entend laquelle de vos deux langues est parlée et traduit dans l'autre. Deux personnes parlent simplement à tour de rôle."),
 next_="Depuis son lancement en août, Prau a reçu plus d'une douzaine de mises à jour : sous-titres en mode Stream, Siri et le bouton Action, résumés de conversation, détection automatique de la langue. Chaque version rend aussi la reconnaissance et la traduction plus rapides et plus précises — et les prochaines fonctions sont déjà en préparation.",
)

U["es"] = dict(
 see_sub="Cada pantalla de abajo es Prau tal como funciona hoy en un iPhone.",
 setup_sub="Hazlo una vez en casa con Wi-Fi: unos minutos en total. Después todo funciona sin ninguna red.",
 voice=("Entrada de voz: se descarga en el propio Prau",
        "Prau descarga por sí mismo el modelo de reconocimiento de voz de cada idioma: durante la primera configuración o más tarde en Prau → Ajustes → Idiomas, tocando el micrófono con un más junto al idioma. No hay que cambiar nada en los Ajustes del iPhone. Un micrófono verde significa que el idioma está listo para la voz."),
 tip="La traducción de texto y fotos no necesita el modelo de voz: funciona en cuanto están los paquetes.",
 faq0="El modelo de voz de ese idioma todavía no está en tu iPhone. Abre Prau → Ajustes → Idiomas y toca el micrófono junto al idioma: Prau lo descarga, más rápido con Wi-Fi. Mientras tanto, la traducción de texto y fotos funciona por completo.",
 auto=("🌐", "Detección automática del idioma",
       "Toca el globo en la pantalla principal y olvídate de cambiar de lado: Prau oye cuál de tus dos idiomas se habla y traduce al otro. Dos personas simplemente hablan por turnos."),
 next_="Desde su lanzamiento en agosto, Prau ha tenido más de una docena de actualizaciones: subtítulos en modo Stream, Siri y el botón de acción, resúmenes de conversación, detección automática del idioma. Cada versión además hace el reconocimiento y la traducción más rápidos y precisos, y las próximas funciones ya están en camino.",
)

U["de"] = dict(
 see_sub="Jeder Bildschirm unten ist Prau, so wie es heute auf einem iPhone läuft.",
 setup_sub="Einmal zu Hause im WLAN erledigen – insgesamt ein paar Minuten. Danach funktioniert alles ganz ohne Netz.",
 voice=("Spracheingabe – direkt in Prau geladen",
        "Prau lädt das Spracherkennungsmodell für jede Sprache selbst – bei der ersten Einrichtung oder später unter Prau → Einstellungen → Sprachen: Tippe auf das Mikrofon mit dem Plus neben einer Sprache. In den iPhone-Einstellungen musst du nichts ändern. Ein grünes Mikrofon heißt: Die Sprache ist bereit für Spracheingabe."),
 tip="Text- und Fotoübersetzung brauchen kein Sprachmodell – sie funktionieren, sobald die Pakete da sind.",
 faq0="Das Sprachmodell für diese Sprache ist noch nicht auf deinem iPhone. Öffne Prau → Einstellungen → Sprachen und tippe auf das Mikrofon neben der Sprache – Prau lädt es, am schnellsten im WLAN. Bis dahin funktionieren Text- und Fotoübersetzung vollständig.",
 auto=("🌐", "Automatische Spracherkennung",
       "Tippe auf den Globus auf dem Hauptbildschirm und wechsle nie mehr die Richtung: Prau hört, welche deiner beiden Sprachen gesprochen wird, und übersetzt in die andere. Zwei Menschen sprechen einfach abwechselnd."),
 next_="Seit dem Start im August hat Prau mehr als ein Dutzend Updates bekommen: Untertitel im Stream-Modus, Siri und die Aktionstaste, Gesprächszusammenfassungen, automatische Spracherkennung. Jede Version macht außerdem Erkennung und Übersetzung schneller und genauer – und die nächsten Funktionen sind schon in Arbeit.",
)

U["nl"] = dict(
 see_sub="Elk scherm hieronder is Prau zoals het vandaag op een iPhone draait.",
 setup_sub="Doe het één keer thuis op wifi — een paar minuten in totaal. Daarna werkt alles helemaal zonder netwerk.",
 voice=("Spraakinvoer — direct in Prau gedownload",
        "Prau downloadt het spraakherkenningsmodel voor elke taal zelf — tijdens de eerste installatie of later in Prau → Instellingen → Talen: tik op de microfoon met een plus naast een taal. In de iPhone-instellingen hoef je niets te wijzigen. Een groene microfoon betekent dat de taal klaar is voor spraak."),
 tip="Tekst- en fotovertaling hebben het spraakmodel niet nodig — ze werken zodra de pakketten er zijn.",
 faq0="Het spraakmodel voor die taal staat nog niet op je iPhone. Open Prau → Instellingen → Talen en tik op de microfoon naast de taal — Prau downloadt het, het snelst op wifi. Tot die tijd werken tekst- en fotovertaling volledig.",
 auto=("🌐", "Automatische taalherkenning",
       "Tik op de wereldbol op het hoofdscherm en wissel nooit meer van kant: Prau hoort welke van je twee talen er gesproken wordt en vertaalt naar de andere. Twee mensen praten gewoon om de beurt."),
 next_="Sinds de lancering in augustus heeft Prau meer dan een dozijn updates gehad: ondertitels in Stream-modus, Siri en de actieknop, gesprekssamenvattingen, automatische taalherkenning. Elke versie maakt herkenning en vertaling bovendien sneller en nauwkeuriger — en de volgende functies zijn al in de maak.",
)

U["it"] = dict(
 see_sub="Ogni schermata qui sotto è Prau così come gira oggi su un iPhone.",
 setup_sub="Fallo una volta a casa col Wi-Fi: pochi minuti in tutto. Poi tutto funziona del tutto senza rete.",
 voice=("Input vocale — scaricato direttamente in Prau",
        "Prau scarica da solo il modello di riconoscimento vocale di ogni lingua — durante la prima configurazione, o più tardi in Prau → Impostazioni → Lingue: tocca il microfono con il più accanto a una lingua. Nelle Impostazioni dell'iPhone non c'è nulla da cambiare. Un microfono verde significa che la lingua è pronta per la voce."),
 tip="La traduzione di testo e foto non ha bisogno del modello vocale: funziona appena i pacchetti sono installati.",
 faq0="Il modello vocale di quella lingua non è ancora sul tuo iPhone. Apri Prau → Impostazioni → Lingue e tocca il microfono accanto alla lingua: Prau lo scarica, più in fretta col Wi-Fi. Nel frattempo la traduzione di testo e foto funziona completamente.",
 auto=("🌐", "Rilevamento automatico della lingua",
       "Tocca il globo nella schermata principale e smetti di cambiare verso: Prau sente quale delle tue due lingue viene parlata e traduce nell'altra. Due persone parlano semplicemente a turno."),
 next_="Dal lancio ad agosto Prau ha ricevuto più di una dozzina di aggiornamenti: sottotitoli in modalità Stream, Siri e il tasto Azione, riassunti delle conversazioni, rilevamento automatico della lingua. Ogni versione rende anche riconoscimento e traduzione più rapidi e precisi — e le prossime funzioni sono già in lavorazione.",
)

U["pt"] = dict(
 see_sub="Cada tela abaixo é o Prau como ele roda hoje em um iPhone.",
 setup_sub="Faça uma vez em casa no Wi-Fi — poucos minutos ao todo. Depois tudo funciona totalmente sem rede.",
 voice=("Entrada de voz — baixada direto no Prau",
        "O Prau baixa sozinho o modelo de reconhecimento de voz de cada idioma — na primeira configuração ou depois em Prau → Ajustes → Idiomas: toque no microfone com um mais ao lado de um idioma. Não é preciso mudar nada nos Ajustes do iPhone. Um microfone verde significa que o idioma está pronto para voz."),
 tip="A tradução de texto e fotos não precisa do modelo de voz — funciona assim que os pacotes estão instalados.",
 faq0="O modelo de voz desse idioma ainda não está no seu iPhone. Abra Prau → Ajustes → Idiomas e toque no microfone ao lado do idioma — o Prau baixa, mais rápido no Wi-Fi. Enquanto isso, a tradução de texto e fotos funciona por completo.",
 auto=("🌐", "Detecção automática de idioma",
       "Toque no globo na tela principal e pare de trocar de lado: o Prau ouve qual dos seus dois idiomas está sendo falado e traduz para o outro. Duas pessoas simplesmente falam por turnos."),
 next_="Desde o lançamento em agosto, o Prau já teve mais de uma dúzia de atualizações: legendas no modo Stream, Siri e o botão de Ação, resumos de conversa, detecção automática de idioma. Cada versão também deixa o reconhecimento e a tradução mais rápidos e precisos — e os próximos recursos já estão a caminho.",
)

U["pl"] = dict(
 see_sub="Każdy ekran poniżej to Prau — tak, jak działa dziś na iPhonie.",
 setup_sub="Zrób to raz w domu na Wi-Fi — w sumie kilka minut. Potem wszystko działa całkiem bez sieci.",
 voice=("Wprowadzanie głosowe — pobierane prosto w Prau",
        "Prau sam pobiera model rozpoznawania mowy dla każdego języka — podczas pierwszej konfiguracji lub później w Prau → Ustawienia → Języki: stuknij mikrofon z plusem obok języka. W Ustawieniach iPhone'a nic nie trzeba zmieniać. Zielony mikrofon oznacza, że język jest gotowy do mowy."),
 tip="Tłumaczenie tekstu i zdjęć nie potrzebuje modelu mowy — działa, gdy tylko pakiety są pobrane.",
 faq0="Modelu mowy dla tego języka nie ma jeszcze na iPhonie. Otwórz Prau → Ustawienia → Języki i stuknij mikrofon obok języka — Prau go pobierze, najszybciej na Wi-Fi. Do tego czasu tłumaczenie tekstu i zdjęć działa w pełni.",
 auto=("🌐", "Automatyczne rozpoznawanie języka",
       "Stuknij globus na ekranie głównym i przestań przełączać kierunek: Prau słyszy, którym z dwóch języków ktoś mówi, i tłumaczy na drugi. Dwie osoby po prostu mówią na zmianę."),
 next_="Od premiery w sierpniu Prau dostał ponad tuzin aktualizacji: napisy w trybie Stream, Siri i przycisk czynności, streszczenia rozmów, automatyczne rozpoznawanie języka. Każda wersja przyspiesza też rozpoznawanie i tłumaczenie oraz czyni je dokładniejszymi — a kolejne funkcje są już w przygotowaniu.",
)

U["tr"] = dict(
 see_sub="Aşağıdaki her ekran, bugün bir iPhone'da çalışan haliyle Prau.",
 setup_sub="Bunu bir kez evde Wi-Fi'deyken yap — toplamda birkaç dakika. Sonrası tamamen ağsız çalışır.",
 voice=("Sesli giriş — doğrudan Prau'da indirilir",
        "Prau her dilin konuşma tanıma modelini kendisi indirir — ilk kurulumda ya da sonradan Prau → Ayarlar → Diller'de: dilin yanındaki artılı mikrofona dokun. iPhone Ayarları'nda hiçbir şeyi değiştirmen gerekmez. Yeşil mikrofon, dilin sesli kullanıma hazır olduğu anlamına gelir."),
 tip="Metin ve fotoğraf çevirisi ses modeline ihtiyaç duymaz — paketler iner inmez çalışır.",
 faq0="O dilin ses modeli henüz iPhone'unda yok. Prau → Ayarlar → Diller'i aç ve dilin yanındaki mikrofona dokun — Prau modeli indirir, en hızlısı Wi-Fi'de. O zamana kadar metin ve fotoğraf çevirisi tam olarak çalışır.",
 auto=("🌐", "Otomatik dil algılama",
       "Ana ekrandaki küreye dokun ve yön değiştirmeyi bırak: Prau iki dilinden hangisinin konuşulduğunu duyar ve diğerine çevirir. İki kişi sadece sırayla konuşur."),
 next_="Ağustostaki çıkışından bu yana Prau bir düzineden fazla güncelleme aldı: Stream modunda altyazılar, Siri ve İşlem düğmesi, konuşma özetleri, otomatik dil algılama. Her sürüm ayrıca tanıma ve çeviriyi daha hızlı ve daha doğru hale getiriyor — sıradaki özellikler de şimdiden hazırlanıyor.",
)

U["ar"] = dict(
 see_sub="كل شاشة أدناه هي Prau كما يعمل على iPhone اليوم.",
 setup_sub="افعل ذلك مرة واحدة في البيت عبر Wi-Fi — بضع دقائق فقط. بعدها يعمل كل شيء دون أي شبكة.",
 voice=("الإدخال الصوتي — يُنزَّل داخل Prau مباشرة",
        "ينزّل Prau بنفسه نموذج التعرّف على الكلام لكل لغة — أثناء الإعداد الأول، أو لاحقًا في Prau ← الإعدادات ← اللغات: اضغط على الميكروفون الذي يحمل علامة زائد بجانب اللغة. لا حاجة لتغيير أي شيء في إعدادات iPhone. الميكروفون الأخضر يعني أن اللغة جاهزة للصوت."),
 tip="ترجمة النص والصور لا تحتاج إلى نموذج الصوت — تعمل بمجرد تنزيل الحزم.",
 faq0="نموذج الصوت لهذه اللغة ليس على iPhone بعد. افتح Prau ← الإعدادات ← اللغات واضغط على الميكروفون بجانب اللغة — سينزّله Prau، والأسرع عبر Wi-Fi. وحتى ذلك الحين تعمل ترجمة النص والصور كاملةً.",
 auto=("🌐", "التعرّف التلقائي على اللغة",
       "اضغط على الكرة الأرضية في الشاشة الرئيسية ولا تبدّل الاتجاه بعد الآن: يسمع Prau أيّ لغتيك يُتحدَّث بها ويترجم إلى الأخرى. يتحدث الشخصان بالتناوب فحسب."),
 next_="منذ إطلاقه في أغسطس حصل Prau على أكثر من اثني عشر تحديثًا: ترجمة نصية حيّة في وضع Stream، وSiri وزر الإجراء، وملخصات المحادثات، والتعرّف التلقائي على اللغة. وكل إصدار يجعل التعرّف والترجمة أسرع وأدق — والميزات التالية قيد العمل بالفعل.",
)

U["zh"] = dict(
 see_sub="下面的每个屏幕都是今天在 iPhone 上运行的 Prau。",
 setup_sub="在家连 Wi-Fi 做一次即可——总共几分钟。之后一切都无需任何网络。",
 voice=("语音输入——直接在 Prau 里下载",
        "Prau 会自己下载每种语言的语音识别模型——在首次设置时，或之后在 Prau → 设置 → 语言中点按语言旁带加号的麦克风即可。无需更改 iPhone 设置。绿色麦克风表示该语言已可使用语音。"),
 tip="文字和照片翻译不需要语音模型——语言包一就绪就能用。",
 faq0="该语言的语音模型还不在你的 iPhone 上。打开 Prau → 设置 → 语言，点按该语言旁的麦克风——Prau 会下载它，连 Wi-Fi 时最快。在此之前，文字和照片翻译完全可用。",
 auto=("🌐", "自动识别语言",
       "点按主屏幕上的地球图标，从此不必再切换方向：Prau 能听出两种语言中正在说的是哪一种，并翻译成另一种。两个人只需轮流说话。"),
 next_="自 8 月上线以来，Prau 已推出十多次更新：Stream 模式实时字幕、Siri 与操作按钮、对话摘要、自动识别语言。每个版本还让识别和翻译更快、更准——下一批功能也已在开发中。",
)

U["zh-hant"] = dict(
 see_sub="下面的每個畫面都是今天在 iPhone 上執行的 Prau。",
 setup_sub="在家用 Wi-Fi 做一次即可——總共幾分鐘。之後一切都不需要任何網路。",
 voice=("語音輸入——直接在 Prau 裡下載",
        "Prau 會自己下載每種語言的語音辨識模型——在首次設定時，或之後在 Prau → 設定 → 語言中點一下語言旁帶加號的麥克風即可。不必更改 iPhone 設定。綠色麥克風代表該語言已可使用語音。"),
 tip="文字和照片翻譯不需要語音模型——語言包一就緒就能用。",
 faq0="該語言的語音模型還不在你的 iPhone 上。打開 Prau → 設定 → 語言，點一下該語言旁的麥克風——Prau 會下載它，連 Wi-Fi 時最快。在此之前，文字和照片翻譯完全可用。",
 auto=("🌐", "自動辨識語言",
       "點一下主畫面上的地球圖示，從此不必再切換方向：Prau 能聽出兩種語言中正在說的是哪一種，並翻譯成另一種。兩個人只要輪流說話。"),
 next_="自 8 月上架以來，Prau 已推出十多次更新：Stream 模式即時字幕、Siri 與動作按鈕、對話摘要、自動辨識語言。每個版本也讓辨識和翻譯更快、更準——下一批功能也已在開發中。",
)

U["ja"] = dict(
 see_sub="以下の画面はすべて、今日iPhoneで動いているPrauそのものです。",
 setup_sub="自宅のWi-Fiで一度だけ——全部で数分です。あとは電波ゼロでもすべて動きます。",
 voice=("音声入力——Prauの中で直接ダウンロード",
        "各言語の音声認識モデルはPrauが自分でダウンロードします——初回の設定時、またはあとから Prau → 設定 → 言語 で言語の横にあるプラス付きのマイクをタップ。iPhoneの設定を変える必要はありません。緑のマイクが付けば、その言語は音声で使えます。"),
 tip="テキストと写真の翻訳には音声モデルは不要です——言語パックが入ればすぐに使えます。",
 faq0="その言語の音声モデルがまだiPhoneにありません。Prau → 設定 → 言語 を開き、言語の横のマイクをタップしてください——Prauがダウンロードします（Wi-Fiが最速）。それまでもテキストと写真の翻訳はすべて使えます。",
 auto=("🌐", "言語の自動判別",
       "メイン画面の地球儀をタップすれば、もう向きを切り替える必要はありません。Prauが2つの言語のどちらが話されたかを聞き分け、もう一方に翻訳します。2人は交互に話すだけです。"),
 next_="8月のリリース以来、Prauは十数回のアップデートを重ねてきました：Streamモードのライブ字幕、Siriとアクションボタン、会話の要約、言語の自動判別。リリースのたびに認識と翻訳もより速く、より正確になっています——次の機能もすでに開発中です。",
)

U["ko"] = dict(
 see_sub="아래 모든 화면은 오늘 iPhone에서 돌아가는 Prau 그대로입니다.",
 setup_sub="집에서 Wi-Fi로 한 번만 해 두세요 — 다 합쳐 몇 분이면 됩니다. 이후에는 네트워크가 전혀 없어도 모든 것이 동작합니다.",
 voice=("음성 입력 — Prau에서 바로 다운로드",
        "Prau가 언어별 음성 인식 모델을 직접 내려받습니다 — 처음 설정할 때, 또는 나중에 Prau → 설정 → 언어에서 언어 옆의 플러스 마이크를 탭하면 됩니다. iPhone 설정에서 바꿀 것은 없습니다. 초록 마이크가 보이면 그 언어는 음성으로 쓸 준비가 된 것입니다."),
 tip="텍스트와 사진 번역에는 음성 모델이 필요 없습니다 — 언어 팩만 받으면 바로 됩니다.",
 faq0="그 언어의 음성 모델이 아직 iPhone에 없습니다. Prau → 설정 → 언어를 열고 언어 옆의 마이크를 탭하세요 — Prau가 내려받으며 Wi-Fi에서 가장 빠릅니다. 그동안에도 텍스트와 사진 번역은 모두 됩니다.",
 auto=("🌐", "언어 자동 감지",
       "메인 화면의 지구본을 탭하면 더 이상 방향을 바꿀 필요가 없습니다: Prau가 두 언어 중 어느 쪽으로 말하는지 알아듣고 다른 언어로 번역합니다. 두 사람은 번갈아 말하기만 하면 됩니다."),
 next_="8월 출시 이후 Prau는 십여 차례 업데이트되었습니다: Stream 모드 실시간 자막, Siri와 동작 버튼, 대화 요약, 언어 자동 감지. 릴리스마다 인식과 번역도 더 빠르고 정확해지고 있으며 — 다음 기능도 이미 개발 중입니다.",
)

U["id"] = dict(
 see_sub="Setiap layar di bawah adalah Prau sebagaimana berjalan di iPhone hari ini.",
 setup_sub="Lakukan sekali di rumah dengan Wi-Fi — total hanya beberapa menit. Setelah itu semuanya berfungsi tanpa jaringan sama sekali.",
 voice=("Input suara — diunduh langsung di Prau",
        "Prau mengunduh sendiri model pengenalan suara untuk tiap bahasa — saat penyiapan pertama, atau nanti di Prau → Pengaturan → Bahasa: ketuk mikrofon bertanda plus di samping bahasa. Tidak ada yang perlu diubah di Pengaturan iPhone. Mikrofon hijau berarti bahasa siap untuk suara."),
 tip="Terjemahan teks dan foto tidak memerlukan model suara — langsung berfungsi begitu paket terpasang.",
 faq0="Model suara untuk bahasa itu belum ada di iPhone Anda. Buka Prau → Pengaturan → Bahasa dan ketuk mikrofon di samping bahasa — Prau akan mengunduhnya, tercepat lewat Wi-Fi. Sementara itu, terjemahan teks dan foto berfungsi penuh.",
 auto=("🌐", "Deteksi bahasa otomatis",
       "Ketuk bola dunia di layar utama dan berhenti mengganti arah: Prau mendengar bahasa mana dari dua bahasa Anda yang diucapkan dan menerjemahkannya ke yang lain. Dua orang cukup berbicara bergantian."),
 next_="Sejak diluncurkan pada Agustus, Prau sudah mendapat lebih dari selusin pembaruan: subtitle di mode Stream, Siri dan tombol Tindakan, ringkasan percakapan, deteksi bahasa otomatis. Setiap rilis juga membuat pengenalan dan terjemahan lebih cepat dan akurat — dan fitur berikutnya sudah dikerjakan.",
)

U["th"] = dict(
 see_sub="ทุกหน้าจอด้านล่างคือ Prau อย่างที่ทำงานบน iPhone ในวันนี้",
 setup_sub="ทำครั้งเดียวที่บ้านผ่าน Wi-Fi — รวมแล้วไม่กี่นาที หลังจากนั้นทุกอย่างทำงานได้โดยไม่ต้องมีเครือข่ายเลย",
 voice=("การป้อนด้วยเสียง — ดาวน์โหลดในแอป Prau ได้เลย",
        "Prau ดาวน์โหลดโมเดลการรู้จำเสียงพูดของแต่ละภาษาเอง — ระหว่างการตั้งค่าครั้งแรก หรือภายหลังใน Prau → การตั้งค่า → ภาษา: แตะไมโครโฟนที่มีเครื่องหมายบวกข้างภาษานั้น ไม่ต้องเปลี่ยนอะไรในการตั้งค่าของ iPhone ไมโครโฟนสีเขียวหมายความว่าภาษานั้นพร้อมใช้เสียงแล้ว"),
 tip="การแปลข้อความและภาพถ่ายไม่ต้องใช้โมเดลเสียง — ใช้งานได้ทันทีที่ชุดภาษาพร้อม",
 faq0="ยังไม่มีโมเดลเสียงของภาษานั้นใน iPhone เปิด Prau → การตั้งค่า → ภาษา แล้วแตะไมโครโฟนข้างภาษานั้น — Prau จะดาวน์โหลดให้ เร็วสุดเมื่อต่อ Wi-Fi ระหว่างนี้การแปลข้อความและภาพถ่ายใช้งานได้เต็มที่",
 auto=("🌐", "ตรวจจับภาษาอัตโนมัติ",
       "แตะลูกโลกบนหน้าจอหลักแล้วไม่ต้องสลับทิศทางอีก: Prau ฟังออกว่ากำลังพูดภาษาไหนในสองภาษาของคุณ แล้วแปลเป็นอีกภาษาหนึ่ง สองคนแค่ผลัดกันพูด"),
 next_="ตั้งแต่เปิดตัวในเดือนสิงหาคม Prau ได้รับการอัปเดตมากกว่าสิบครั้ง: คำบรรยายสดในโหมด Stream, Siri และปุ่มแอ็กชัน, สรุปบทสนทนา, ตรวจจับภาษาอัตโนมัติ ทุกรุ่นยังทำให้การรู้จำและการแปลเร็วและแม่นยำขึ้น — และฟีเจอร์ถัดไปก็กำลังพัฒนาอยู่แล้ว",
)

U["vi"] = dict(
 see_sub="Mọi màn hình bên dưới đều là Prau đúng như đang chạy trên iPhone hôm nay.",
 setup_sub="Làm một lần ở nhà với Wi-Fi — tổng cộng vài phút. Sau đó mọi thứ chạy mà không cần mạng chút nào.",
 voice=("Nhập bằng giọng nói — tải ngay trong Prau",
        "Prau tự tải mô hình nhận dạng giọng nói cho từng ngôn ngữ — trong lần thiết lập đầu tiên, hoặc sau đó trong Prau → Cài đặt → Ngôn ngữ: chạm vào micrô có dấu cộng cạnh ngôn ngữ. Không cần thay đổi gì trong Cài đặt của iPhone. Micrô xanh lá nghĩa là ngôn ngữ đã sẵn sàng cho giọng nói."),
 tip="Dịch văn bản và ảnh không cần mô hình giọng nói — dùng được ngay khi đã có gói ngôn ngữ.",
 faq0="Mô hình giọng nói của ngôn ngữ đó chưa có trên iPhone. Mở Prau → Cài đặt → Ngôn ngữ và chạm vào micrô cạnh ngôn ngữ — Prau sẽ tải về, nhanh nhất khi có Wi-Fi. Trong lúc chờ, dịch văn bản và ảnh vẫn hoạt động đầy đủ.",
 auto=("🌐", "Tự nhận diện ngôn ngữ",
       "Chạm vào quả địa cầu trên màn hình chính và không cần đổi chiều nữa: Prau nghe ra bạn đang nói ngôn ngữ nào trong hai ngôn ngữ và dịch sang ngôn ngữ kia. Hai người chỉ cần nói lần lượt."),
 next_="Từ khi ra mắt vào tháng 8, Prau đã có hơn chục bản cập nhật: phụ đề ở chế độ Stream, Siri và nút Tác vụ, tóm tắt cuộc trò chuyện, tự nhận diện ngôn ngữ. Mỗi bản phát hành còn giúp nhận dạng và dịch nhanh hơn, chính xác hơn — và các tính năng tiếp theo đã đang được phát triển.",
)

# 14.11 (2): глобус — полноценный ряд со скриншотом (img/auto), alt по языкам.
ALT_AUTO = {
 "en": "The globe is on: English and French phrases from one conversation, each translated into the other language",
 "ru": "Глобус включён: фразы на английском и французском из одного разговора, каждая переведена на другой язык",
 "uk": "Глобус увімкнено: фрази англійською та французькою з однієї розмови, кожна перекладена іншою мовою",
 "fr": "Globe activé : phrases en anglais et en français d’une même conversation, chacune traduite dans l’autre langue",
 "es": "Globo activado: frases en inglés y en francés de una misma conversación, cada una traducida al otro idioma",
 "de": "Globus aktiv: englische und französische Sätze aus einem Gespräch, jeweils in die andere Sprache übersetzt",
 "nl": "Wereldbol aan: Engelse en Franse zinnen uit één gesprek, elk vertaald naar de andere taal",
 "it": "Globo attivo: frasi in inglese e in francese della stessa conversazione, ognuna tradotta nell’altra lingua",
 "pt": "Globo ativado: frases em inglês e em francês da mesma conversa, cada uma traduzida para o outro idioma",
 "pl": "Globus włączony: zdania po angielsku i po francusku z jednej rozmowy, każde przetłumaczone na drugi język",
 "tr": "Küre açık: aynı konuşmadan İngilizce ve Fransızca cümleler, her biri diğer dile çevrilmiş",
 "ar": "الكرة الأرضية مفعّلة: عبارات بالإنجليزية والفرنسية من محادثة واحدة، كلٌّ منها مترجمة إلى اللغة الأخرى",
 "zh": "地球图标已开启：同一段对话中的英语和法语句子，各自被翻译成另一种语言",
 "zh-hant": "地球圖示已開啟：同一段對話中的英語和法語句子，各自被翻譯成另一種語言",
 "ja": "地球儀オン：ひとつの会話の英語とフランス語のフレーズが、それぞれもう一方の言語に翻訳されている",
 "ko": "지구본 켜짐: 한 대화 속 영어와 프랑스어 문장이 각각 다른 언어로 번역된 화면",
 "id": "Ikon globe aktif: kalimat bahasa Inggris dan Prancis dari satu percakapan, masing-masing diterjemahkan ke bahasa lainnya",
 "th": "เปิดลูกโลกแล้ว: ประโยคภาษาอังกฤษและฝรั่งเศสจากบทสนทนาเดียวกัน แต่ละประโยคแปลเป็นอีกภาษาหนึ่ง",
 "vi": "Đã bật quả địa cầu: các câu tiếng Anh và tiếng Pháp trong cùng một cuộc trò chuyện, mỗi câu được dịch sang ngôn ngữ kia",
}
assert set(ALT_AUTO) == set(U)
