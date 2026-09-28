# Exam Workflow — Unity 2022.3.40f1 (Trần Thiên Bảo, 23632721)

Use this when the real exam question arrives. The real exam question is the **only** source of
requirements. W1–W5 (`Reference_W1_W5/`) are reference examples only; the exam may be completely different.

## Standard flow

```
Real Exam Question
→ Analyze every requirement
→ Do NOT assume similarity to W1-W5
→ Inspect current repository
→ Decide what can be reused
→ Plan minimal changes
→ Implement only required features
→ Verify scripts
→ Verify scene setup
→ Verify Inspector references
→ Verify Play Mode
→ Verify build configuration
→ Report changed files
→ Give step-by-step instructions for the student
```

## Step details

1. **Analyze every requirement.** Split the question into a numbered list of concrete, checkable
   requirements (objects, behaviours, UI, inputs, text, colours, build/platform, deliverables).
   Mark anything ambiguous and ask the student instead of guessing.
2. **Do not assume similarity to W1–W5.** Use them only for style and level. Never add a feature
   because "W4 had it".
3. **Inspect the current repository.** Read `CLAUDE.md` (especially §6 Packages and §9 Known
   Issues), `Packages/manifest.json`, the scenes and scripts. Check whether the student has already
   committed the Unity-generated files (ProjectSettings, `.meta`, `Assets/TextMesh Pro/`).
4. **Decide what can be reused.** Existing scripts, scenes, sprites, or none. Keep the sample
   scenes unless the exam requires changing them.
5. **Plan minimal changes.** List which files will be created/modified, which scene(s) the exam
   runs in, which built-in modules/packages are needed (e.g. `com.unity.modules.physics` for
   Rigidbody/Collider; see `CLAUDE.md` §6), and what the student must do in the Editor.
6. **Implement only required features.** Simple `MonoBehaviour`s, file name = class name,
   clear Inspector fields, no extra frameworks or packages.
7. **Verify scripts.** No compile errors (a single error blocks Play Mode for the whole project);
   every API used is available with the enabled modules; `using` directives present; Unity 2022.3 APIs.
8. **Verify scene setup.** Camera present (3D/2D), Light where needed, EventSystem for any UI
   interaction, objects named clearly, scene saved and listed in Build Settings.
9. **Verify Inspector references.** Every public/`[SerializeField]` field that must be assigned is
   listed for the student with "drag X into field Y on object Z"; add null checks with a clear
   `Debug.LogError` where a missing reference would otherwise fail silently.
10. **Verify Play Mode.** Only possible in the Unity Editor. A cloud session must say "not tested in
    Unity" and give the student an exact test script: *press Play → do X → expect Y*.
11. **Verify build configuration.** Scenes in File → Build Settings (correct order), target
    platform, player settings required by the exam.
12. **Report changed files.** Every file created / modified / deleted, and why.
13. **Give step-by-step instructions** for opening, setting up, running and (if required) building
    the result on the school computer.

## Rules

- The real exam is the source of truth; W1–W5 are reference examples only.
- Keep solutions simple, reliable and explainable by a beginner.
- Avoid unnecessary packages and architecture; enable a module only for a stated requirement.
- Do not break existing working functionality unless the exam requires it.
- Never invent unspecified requirements.
- Never claim testing that was not actually performed.
- Report anything that could not be verified.

## Final report format (for Claude)

1. Requirements understood (numbered, from the exam text)
2. Implementation completed (requirement → how it is implemented)
3. Files created
4. Files modified
5. Scenes changed/created
6. Packages/modules required (and whether they were enabled)
7. Inspector/setup instructions for the student
8. How to run (and build, if required)
9. Verification status: what was verified, how, and what was NOT verified
10. Remaining limitations

---

## Student checklist (short)

**Before the exam (once, at home or on the school PC)**
- [ ] Unity Hub has **2022.3.40f1** installed (or another 2022.3.x; never Unity 6).
- [ ] Project opens, Console shows **0 red errors**.
- [ ] TMP Essentials imported (Window → TextMeshPro → Import TMP Essential Resources).
- [ ] Generated files committed and pushed: `ProjectSettings/*.asset`, all new `.meta` files,
      `Packages/packages-lock.json`, `Assets/TextMesh Pro/`.
- [ ] You know how to pull the latest version (`git pull`, or GitHub → Code → Download ZIP).

**During the exam**
- [ ] Paste the real question into `CLAUDE_TASK_TEMPLATE.md` and give it to Claude.
- [ ] Check Claude's requirement list against the question; correct anything misunderstood.
- [ ] Pull the changes, let Unity recompile, check the Console for **0 errors**.
- [ ] If Claude says a module/package is needed, enable it (Window → Package Manager → Built-in).
- [ ] Do Claude's Inspector steps exactly (drag references, add EventSystem/Camera if told).
- [ ] Press Play and test **every** requirement yourself, one by one.
- [ ] Save the scene (Ctrl+S) and the project (File → Save Project).
- [ ] If a build is required: File → Build Settings → Add Open Scenes → Build into `Build/`.
- [ ] Submit in the format the teacher asks for (project folder/ZIP/build). Do not include `Library/`
      unless told to.
