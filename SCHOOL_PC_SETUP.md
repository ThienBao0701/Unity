# School Computer Setup — Unity 2022.3.40f1

## 1. Get the project

- **With Git:** `git clone https://github.com/ThienBao0701/Unity.git C:\Unity\Exam23632721`
  (later: `git pull` inside that folder to get new changes).
- **Without Git:** GitHub → *Code* → *Download ZIP* → extract.
- Use a **short path with no spaces or Vietnamese characters** (e.g. `C:\Unity\Exam23632721`).
  Do not use OneDrive/Desktop-synced folders.

## 2. Open it

1. Unity Hub → **Installs**: check that **2022.3.40f1** is installed.
   - Another **2022.3.x** is usually fine: Hub asks to change the version → *Continue*.
   - **Do not open with Unity 6 / 2023.x.** It upgrades the project.
2. Unity Hub → **Projects** → **Add** → *Add project from disk* → select the folder that contains
   `Assets`, `Packages`, `ProjectSettings`.
3. Open it. **Be online the first time.** Unity downloads TextMeshPro 3.0.6 unless it is cached.
   The first import takes a few minutes. Unity also creates missing settings and `.meta` files.

## 3. First-open checks

1. **Window → General → Console**: there must be **0 red errors**. If Unity offers *Safe Mode*,
   choose it and read the Console errors.
2. **Window → TextMeshPro → Import TMP Essential Resources** → *Import*. (This window also pops up
   automatically the first time text is created.) Without it, text is invisible.
3. Open `Assets/Scenes/01_CustomMathDuel.unity` → **Play**: the Math Duel screen should appear.
   Known sample limitations: no EventSystem, so buttons do not click; no Camera, so the Game view says
   "No cameras rendering". Scene 02 = scene 01. Scene 03 is a placeholder. See `CLAUDE.md` §9.
4. If using Git, **commit and push the files Unity generated** so every computer is identical:
   `ProjectSettings/*.asset`, new `.meta` files, `Packages/packages-lock.json`, `Assets/TextMesh Pro/`.

## 4. Things this project does NOT have enabled

This project uses a **reduced package list**. If the exam needs one of these, enable it via
**Window → Package Manager → Packages: Built-in → select → Enable**:

| Needed for | Built-in module |
|---|---|
| Rigidbody, 3D colliders, collisions, CharacterController | Physics |
| Animator / animations | Animation |
| NavMeshAgent | AI |
| Particle System | Particle System |

- **Visual Studio IntelliSense:** Package Manager → *Unity Registry* → **Visual Studio Editor** →
  Install, then Edit → Preferences → External Tools → select Visual Studio.
- Install anything else only if the real exam requires it.

## 5. Build (only if the exam asks)

File → Build Settings → **Add Open Scenes** (the list starts empty) → choose platform →
**Build** into a folder named `Build/` (ignored by Git). Android/iOS builds need the matching
*Build Support* module installed for 2022.3.40f1 in Unity Hub.
