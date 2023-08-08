import json


idb_v1 = {
    "Техническая": {
        "Программирование на Scratch": [
            "Сформировать интерес к программированию",
            "Научить основам алгоритмизации и языка программирования Scratch",
            "Сформировать навык разработки проектов в среде Scratch",
            "Совершенствовать ключевые компетенции программирования в Scratch"
        ],
        "Программирование на Python": [
            "Сформировать интерес к программированию",
            "Научить основам программирования на Python",
            "Сформировать навык разработки проектов на Python",
            "Совершенствовать ключевые компетенции программирования на Python"

        ],
        "Управление беспилотными летательными аппаратами": [
            "Научить основам пилотирования БПЛА",
            "Научить основам FPV пилотирования и обслуживания БПЛА на практике",
            "Научить основам аэрофотосъёмки и фотограмметрии",
            "Научить основам автономного пилотирования БПЛА",
            "Развивать навык  пилотирования  и эксплуатации БПЛА"
        ],
        "Робототехника Lego WeDo": [
            "Сформировать интерес к робототехнике",
            "Научить основам алгоритмизации и программирования робототехнических устройств",
            "Научить проектировать и создавать робототехнические устройства",
            "Совершенствовать ключевые компетенции по созданию робототехнических проектов"
        ],
        "Робототехника Lego EV": [
            "Сформировать интерес к робототехнике",
            "Научить основам алгоритмизации и программирования робототехнических устройств",
            "Сформировать навык разработки робототехнических проектов",
            "Совершенствовать ключевые компетенции  по созданию робототехнических проектов"
        ],
        "3D моделирование и 3D печать": [
            "Сформировать интерес к 3D моделированию",
            "Научить основам 3D моделирования",
            "Сформировать базовые знания и умения в трехмерной графике",
            "Сформировать начальные умения в трехмерной печати"
        ]
    },
    "Художественная":{
        "Театр": [
            "Сформировать общее представление о театре",
            "Научить основам актерского мастерства",
            "Научить практическим навыкам сценической речи и работы с художественным текстом",
            "Обучить основам сценического движения",
            "Сформировать навыки театрально-исполнительской деятельности",
            "Научить основам сценографии",
            "Научить основам кукловождения и способам изготовления кукол",
            "Вовлечь в социально-значимую деятельность"
        ]
    },
    "Туристско-краеведческая": {
        "Основы туризма": [
            "Научить основам туристской подготовки",
            "Научить основам гигиены и первой доврачебной помощи",
            "Научить основам топографии и ориентирования",
            "Научить основам краеведения"
        ],
        "Краеведение": [
            "Изучить историю Хабаровского края",
            "Познакомить с этнографией коренных малых народов севера, проживающих в Хабаровском крае",
            "Познакомить с флорой и фауной Хабаровского края",
            "Изучить географию Хабаровского края"
        ],
        "Школа безопасности": [
            "Научить основам безопасности жизнедеятельности",
            "Научить правильному поведению в чрезвычайных ситуациях",
            "Сформировать первичные умения по оказанию первой доврачебной помощи",
            "Научить основам пожарно-прикладного и спасательного спорта (ППС)"
        ],
        "Музейное дело": [
            "Изучить основы музейного дела",
            "Познакомить с правилами комплектования и работы с музейными фондами",
            "Научить основам экскурсионной работы",
            "Организовать исследовательскую деятельность в школьном музее",
            
        ]
    },
    "Физкультурно-спортивная": {
        "Вольная борьба": [
            "Научить основам вольной борьбы",
            "Способствовать развитию общей физической подготовки",
            "Обучить основам специальной физической подготовки",
            "Обучить навыкам техники и тактики ведения схватки на соревнованиях"
        ],
        "Баскетбол": [
            "Познакомить учащихся с видом спорта «Баскетбол», правилами игры, техникой, тактикой, правилами судейства и организацией проведения соревнований, мерами безопасности на занятиях",
            "Способствовать развитию физических качеств, необходимых для успешной игры в баскетбол",
            "Познакомить с техническими и тактическими приемами баскетбола",
            "Способствовать формированию соревновательного опыта"
        ],
        "Лёгкая отлетика": [
            "Обучить необходимым понятиям и теоретическим сведениям по физической культуре и спорту",
            "Развивать основные физические качества",
            "Развивать физические качества, специальные двигательные навыки",
            "Повысить техническую подготовленность в данном виде спорта"
        ],
        "Киокушинкай": [
            "Познакомить с терминами, общими понятиями, техникой безопасности, историей, основными направлениями и техниками киокусинкай",
            "Способствовать развитию общей физической подготовки (ОФП)",
            "Научить основам специальной физической подготовки (СФП)",
            "Научить базовым техникам киокусинкай"
        ]
    },
    "Социально-гуманитарная": {
            "Медиацентр":[
                "Сформировать общее представление о журналистике и особенностях профессии «журналист»",
                "Познакомить с направлением журналистики «периодическая печать»",
                "Научить основам фотожурналистики",
                "Научить основам тележурналистики",
                "Научить основам операторского мастерства и видеомонтажа",
                "Научить основам радиожурналистики",
                "Познакомить с формами интернет-журналистики",
                "Познакомить с основами организации работы медиацентра в школе"
            ]
    }
}
