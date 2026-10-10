# Партнёрские ссылки Prau — как завести партнёра

Ссылка партнёра: `https://getprau.com/go/<slug>/` — одна на человека.
Три кнопки ведут на три оффера Apple с его именем. Покупка в отчётах Apple и RevenueCat помечается именем оффера.

## 1. App Store Connect (под Alexander, Admin)

На каждого партнёра — три оффера. **Reference name = имя партнёра**: именно оно приходит в транзакцию.

| Продукт | Reference name | Тип оффера | Custom code |
|---|---|---|---|
| Annual (`com.liliia.prau.pro.annual`) | `partner_maria_annual` | Бесплатно, 1 неделя, новые подписчики | `MARIAYEAR` |
| Monthly (`com.liliia.prau.pro.monthly`) | `partner_maria_monthly` | Бесплатно, 1 неделя, новые подписчики | `MARIAMONTH` |
| Lifetime (`com.liliia.prau.pro.lifetime`) | `partner_maria_lifetime` | Скидка 10% | `MARIALIFE` |

- Коды: только латинские буквы и цифры, уникальные в приложении. Лимит использований — с запасом (например, 10 000).
- Срок действия — до 31.03.2027 или «без срока», если ASC позволит.
- Лимит: около 10 активных офферов на **каждый** продукт → одновременно около 10 партнёров.

## 2. Сайт

1. Добавить строку в `gen/partners.csv`:
   `maria,Мария,ru,MARIAYEAR,MARIAMONTH,MARIALIFE`
   Язык (`ru` `uk` `en` `nl` `fr` `de`) — язык по умолчанию: превью в мессенджере и запасной вариант. Страница сама показывает язык телефона, вверху переключатель. Имя пиши так, как его знает аудитория (для Бельгии — латиницей).
2. `python3 gen/build_partners.py` — соберёт `go/maria/` и `qr.png`.
   Для QR один раз: `pip3 install qrcode pillow`.
3. Проверка локально: `python3 -m http.server` → `http://localhost:8000/go/maria/`
4. `git add go gen && git commit -m "partners: maria" && git push`

Коды повторяться не могут — генератор остановится и скажет, где дубль.

## 3. Где смотреть результат

| Что | Где |
|---|---|
| Сколько открыли страницу | Cloudflare → getprau.com → Analytics → путь `/go/maria/` |
| Сколько нажали каждую кнопку | Cloudflare → пути `/go/maria/annual/`, `/monthly/`, `/lifetime/` |
| Сколько активировали код | ASC → продукт → Offer Codes → оффер партнёра |
| Кто оплатил (для выплаты) | ASC → Sales and Trends → Subscription Event report (Annual/Monthly); Sales report (Lifetime); RevenueCat → Customers → история транзакций |

## 4. До запуска первого партнёра — обязательная проверка

Завести партнёра `test` (уже есть в CSV), пройти по ссылке со своего iPhone, купить по каждой кнопке и проверить:

- [ ] открывается App Store с уже подставленным бонусом;
- [ ] Lifetime по коду открывается и показывает цену со скидкой;
- [ ] в RevenueCat и в отчётах ASC видно `partner_test_…` у транзакции — **в каком поле**;
- [ ] Cloudflare показывает заходы по путям `/go/test/…`. Если нет — включить Cloudflare Web Analytics только для `/go/`.

После проверки — отменить тестовые подписки, Lifetime вернуть через reportaproblem.apple.com.
