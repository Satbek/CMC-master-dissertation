# CMC-master-dissertation
ВМК МГУ, кафедра МФ, магистерская диссертация
## Задача восстановления волнового фронта по локальным наклонам

В репозитории находится описание и реализация вариационного
метода восстановления волнового фронта.

Метод основан на МКЭ (метод конечных элементов). Исходно ставится задача минимизации функционала.

<p align="center"><img alt="$$J(u) = \int \limits_0^{2\pi} \int \limits_0^{2\pi} ((u_x - g_1)^2 + (u_y-g_2)^2 + \alpha u^2 )dxdy$$" src="svgs/753f18a4bd90e90c9e89e695d8bda139.svg" align="middle" width="351.8418651pt" height="57.3884685pt"/></p>

Где <img alt="$u$" src="svgs/6dbb78540bd76da3f1625782d42d6d16.svg" align="middle" width="9.4102734pt" height="14.1552444pt"/> - волновой фронт, <img alt="$g_1, g_2$" src="svgs/b46b024eed36ef94110b91fd37f95289.svg" align="middle" width="36.9140541pt" height="14.1552444pt"/> - локальные наклоны, <img alt="$\alpha$" src="svgs/c745b9b57c145ec5577b82542b2df546.svg" align="middle" width="10.57650495pt" height="14.1552444pt"/> - регуляризатор Тихонова.
Решение ищется в пространстве Соболева  <img alt="$W_{2\pi}^{1}(\Omega)$" src="svgs/296f10f4481e13785e18eefa3129932b.svg" align="middle" width="55.65716475pt" height="26.7617526pt"/>, <img alt="$2 \pi$" src="svgs/70f9064f0ff73b7e521f0c1563932b2f.svg" align="middle" width="18.17931555pt" height="21.1872144pt"/> - периодичесих функций.

Далее получаем необходимое условие минимума функционала:

<p align="center"><img alt="$$(u_x, \phi_x) + (u_y,\phi_y) + \alpha(u, \phi) = (g_1, \phi_x) + (g_2, \phi_y),\;\;\forall\phi \in W_{2\pi}^{1}(\Omega)$$" src="svgs/bf8372c9b9142f5706f67e769b54611e.svg" align="middle" width="460.5045885pt" height="18.9059673pt"/></p>

Отсюда применяя МКЭ получаем разностную схему:

<p align="center"><img alt="$$B_2 \Lambda_1 u + B_1 \Lambda_2 u + \alpha B_1 B_2 u = F(g_1,g_2)$$" src="svgs/a088ea13200752a2d02eff39f9374a45.svg" align="middle" width="281.23510635pt" height="16.438356pt"/></p>

Разностная схема решается методом Фурье. В работе будут рассмотрены различные модификации разностной схемы, а также представления локальных наклонов.