# Mapa dos requisitos

| Requisito do professor | Onde é cumprido |
|---|---|
| Sem engine (pygame permitido) | projeto inteiro em pygame-ce |
| Elementos animados | `src/fighter/animation.py` |
| Transformações geométricas (≥ 2) | translação (andar, run, dash, knockback) e escala/flip (encarar o oponente) em `src/fighter/fighter.py` |
| Matrizes de transformação | `src/geometry/mat3.py`, aplicadas em sprites e caixas (`src/physics/boxes.py`) |
| Detecção de colisão própria | `src/physics/collision.py` (AABB à mão) |
| Controle por quadros (passo fixo) | `src/core/game.py` (60 ticks/s) |
| Eventos de teclado/mouse em tempo real | `src/core/input.py` |
| Primitivas gráficas | `src/render/primitives.py` (barra de vida, sombra) e `src/render/debug.py` (caixas) |
