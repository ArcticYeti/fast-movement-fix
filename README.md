# Fast Movement Fix

[![ReaperMC Badge](https://img.shields.io/badge/Powered%20by-ReaperMC-%23ec7210)](https://reapermc.github.io)

> Fix for Minecraft's poor handling of higher movement speeds when falling and jumping


**Vanilla**:

https://www.youtube.com/watch?v=TdFyBfk6YeM

**Fast Movement Fix**:

https://www.youtube.com/watch?v=SEf9PRFqjV8


## Explanation

Sprint-jumping propels us forward at a `0°` angle, directly to the front.

While sprinting and descending, the initial force pushes us forward and into the ground, serving as downforce at an angle of `35°`. This downforce effect was primarily crafted for smoothly navigating 1-2 block descents, ensuring it remains unobtrusive for higher falls.

The intensity of both of these maneuvers dynamically scales up with the player's movement speed.


## Delta Dependency

This project uses the [Delta](https://github.com/BigPapi13/Delta/tree/no-rp) library. It is already included in the datapack out of the box.

If you are currently using the library in your world, please ensure that it is loaded **after** this datapack.


## Data Analysis

In the **Vanilla** state, our travel speed decreases when sprint-jumping, making it slower than walking even at `speed` level `1`.

**Fast Movement Fix** aims to stabilize the speed increase from sprint-jumping at approximately `24%`, which is close to the **Vanilla** state where no `speed` effect is applied (around `21%`).

![vanilla_vs_fmf_data](./resources/vanilla_vs_fmf.png)

The data regarding the initial downforce applied when falling was not measured due to the difficulty of testing. The values were primarily estimated and adjusted based on the feel while traversing various types of terrain.


## Known limitations

- May cause brief visual glitches in Multiplayer (known [delta-no-rp](https://github.com/BigPapi13/Delta/tree/no-rp) issue)
- Only works while sprinting (simpler to implement and more stable)


## Contributing

This project uses [Beet](https://github.com/mcbeet) and needs to be compiled from the source.

1. Install the requirements.
```bash
pip install -r requirements.txt
```
2. Run `beet build` in the terminal.
```bash
beet build
```
3. The compiled datapack will be located under `./dist/`.


## Credits

[BigPapi13](https://github.com/BigPapi13) - [Delta (no-rp)](https://github.com/BigPapi13/Delta/tree/no-rp)

---
License - [MIT](https://github.com/ArcticYeti/fast-movement-fix/blob/main/LICENSE)