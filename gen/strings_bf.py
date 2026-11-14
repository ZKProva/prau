# -*- coding: utf-8 -*-
# 15.11.2026: баннер Чёрной пятницы. Показ только в окне акции — по часам
# посетителя, сверка в UTC: 23.11 00:00 Киев … 02.12 12:00 Киев (= конец 1 декабря
# везде, совпадает с "ends" offering в RevenueCat). До и после — скрыт
# (атрибут hidden в HTML), поисковики его не индексируют как текст страницы.
BF_START = "2026-11-22T22:00:00Z"
BF_END   = "2026-12-02T10:00:00Z"

# (заголовок, текст). Кнопка — x["nav_cta"] страницы (ссылка в App Store).
BF = {
 "en": ("Black Friday: Prau Lifetime −50%",
        "One payment — Prau is yours forever. Through December 1, on the purchase screen in Prau."),
 "ru": ("Чёрная пятница: Prau Lifetime −50%",
        "Один платёж — и Prau ваш навсегда. До 1 декабря включительно, на экране покупки в Prau."),
 "uk": ("Чорна п’ятниця: Prau Lifetime −50%",
        "Один платіж — і Prau ваш назавжди. До 1 грудня включно, на екрані покупки в Prau."),
 "fr": ("Black Friday : Prau Lifetime −50 %",
        "Un seul paiement, Prau est à vous pour toujours. Jusqu’au 1er décembre inclus, sur l’écran d’achat de Prau."),
 "es": ("Black Friday: Prau Lifetime −50 %",
        "Un solo pago y Prau es tuyo para siempre. Hasta el 1 de diciembre incluido, en la pantalla de compra de Prau."),
 "de": ("Black Friday: Prau Lifetime −50 %",
        "Einmal zahlen – Prau gehört dir für immer. Bis einschließlich 1. Dezember, im Kaufbildschirm von Prau."),
 "nl": ("Black Friday: Prau Lifetime −50%",
        "Eén betaling en Prau is voor altijd van jou. Tot en met 1 december, op het aankoopscherm in Prau."),
 "it": ("Black Friday: Prau Lifetime −50%",
        "Un solo pagamento e Prau è tuo per sempre. Fino al 1° dicembre incluso, nella schermata di acquisto di Prau."),
 "pt": ("Black Friday: Prau Lifetime −50%",
        "Um único pagamento e o Prau é seu para sempre. Até 1º de dezembro, na tela de compra do Prau."),
 "pl": ("Black Friday: Prau Lifetime −50%",
        "Jedna płatność i Prau jest Twój na zawsze. Do 1 grudnia włącznie, na ekranie zakupu w Prau."),
 "tr": ("Black Friday: Prau Lifetime %50 indirimli",
        "Tek ödeme, Prau sonsuza dek sizin. 1 Aralık dahil, Prau’daki satın alma ekranında."),
 "ar": ("الجمعة السوداء: Prau Lifetime بخصم 50%",
        "دفعة واحدة ويصبح Prau لك إلى الأبد. حتى 1 ديسمبر، من شاشة الشراء في Prau."),
 "zh": ("黑色星期五：Prau 终身版 5 折",
        "一次付款，Prau 永久归你。截至 12 月 1 日，在 Prau 的购买页面。"),
 "zh-hant": ("黑色星期五：Prau 終身版 5 折",
        "一次付款，Prau 永久屬於你。至 12 月 1 日止，在 Prau 的購買頁面。"),
 "ja": ("ブラックフライデー：Prau 買い切り版が50%オフ",
        "一度の支払いで Prau がずっとあなたのものに。12月1日まで、Prau の購入画面で。"),
 "ko": ("블랙 프라이데이: Prau 평생 이용권 50% 할인",
        "한 번 결제로 Prau를 평생 사용하세요. 12월 1일까지, Prau 구매 화면에서."),
 "id": ("Black Friday: Prau Lifetime −50%",
        "Sekali bayar, Prau milik Anda selamanya. Hingga 1 Desember, di layar pembelian Prau."),
 "th": ("แบล็กฟรายเดย์: Prau Lifetime ลด 50%",
        "จ่ายครั้งเดียว ใช้ Prau ได้ตลอดไป ถึงวันที่ 1 ธันวาคม ที่หน้าซื้อในแอป Prau"),
 "vi": ("Black Friday: Prau Lifetime giảm 50%",
        "Trả một lần, Prau là của bạn mãi mãi. Đến hết ngày 1/12, tại màn hình mua trong Prau."),
}
