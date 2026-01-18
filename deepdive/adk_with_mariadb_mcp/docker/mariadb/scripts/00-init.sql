create table products
(
    id         bigint            not null primary key,
    name       varchar(100)      not null comment '상품명',
    price      int unsigned      not null comment '가격',
    price_sale int unsigned      not null,
    maker      varchar(50)       null comment '제조사',
    state      tinyint default 1 not null comment '판매 상태 (0: 품절, 1: 판매중)'
);



insert into products (id, name, price, price_sale, maker, state)
values (1, '갤럭시 S24 Ultra', 1690000, 1490000, '삼성전자', 1),
       (2, '아이폰 15 Pro', 1550000, 1450000, 'Apple', 1),
       (3, 'LG 그램 17', 2390000, 2190000, 'LG전자', 1),
       (4, '맥북 프로 16인치', 3490000, 3290000, 'Apple', 1),
       (5, '갤럭시 탭 S9', 1290000, 1090000, '삼성전자', 1),
       (6, '아이패드 프로 12.9', 1790000, 1690000, 'Apple', 1),
       (7, '삼성 Neo QLED 8K', 8990000, 7990000, '삼성전자', 1),
       (8, 'LG 올레드 TV 77인치', 7490000, 6990000, 'LG전자', 1),
       (9, '다이슨 V15 무선청소기', 1190000, 990000, 'Dyson', 1),
       (10, '에어팟 프로 2세대', 359000, 329000, 'Apple', 1),
       (11, '갤럭시 버즈 2 Pro', 289000, 249000, '삼성전자', 1),
       (12, '소니 WH-1000XM5', 449000, 399000, 'Sony', 1),
       (13, '닌텐도 스위치 OLED', 428000, 398000, 'Nintendo', 1),
       (14, 'PS5 디지털 에디션', 498000, 478000, 'Sony', 1),
       (15, '로지텍 MX Master 3S', 139000, 119000, 'Logitech', 1),
       (16, '삼성 비스포크 냉장고', 3290000, 2990000, '삼성전자', 1),
       (17, 'LG 트롬 세탁기 21kg', 2190000, 1990000, 'LG전자', 1),
       (18, '쿠쿠 압력밥솥 10인용', 489000, 429000, '쿠쿠', 1),
       (19, '샤오미 공기청정기 4 Pro', 429000, 379000, 'Xiaomi', 0),
       (20, '필립스 에어프라이어', 289000, 259000, 'Philips', 1);