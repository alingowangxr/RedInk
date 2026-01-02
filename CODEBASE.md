# CODEBASE.md

> **Auto-generated project context file.** Refreshed on every session start.
>
> **Purpose:** Provides Claude AI with project structure, OS info, and coding standards automatically.

---

# 📁 Project Context

**Project:** `RedInk`
**Framework:** `python`
**Type:** `python`
**Path:** `C:\Users\mike\RedInk`
**Detected:** 2026-01-03 00:38:35

---

## 🖥️ Operating System

| Property | Value |
|----------|-------|
| **OS** | Windows |
| **Shell** | PowerShell / CMD |

---

## ⚡ Terminal Commands (Current OS)

#### 🪟 Windows Terminal Commands

##### PowerShell
```powershell
ls                    # List files
cd <path>             # Change directory
pwd                   # Current directory
mkdir <dir>            # Create directory
rm <file>             # Remove file
rm -r <dir>           # Remove directory
cat <file>            # View file
echo $env:PATH        # Show environment variables
```

##### Common Tasks
- **File Explorer**: `start .`
- **Open with default app**: `start <file>`
- **Process manager**: `taskmgr` or `Get-Process`
- **Network info**: `ipconfig` or `Get-NetIPAddress`
- **System info**: `systeminfo`

##### Package Managers
```powershell
winget install <app>     # Install application
winget search <app>      # Search for application
winget upgrade <app>     # Upgrade application
winget list              # List installed apps
```

---


## 🎯 Project Environment

| Property | Value |
|----------|-------|
| **Project Type** | PYTHON |
| **Framework** | PYTHON |
| **Platform** | GENERAL |

---

## 📋 Quick Project Commands

#### Python
```bash
pip install -r requirements.txt    # Install dependencies
python manage.py runserver         # Django dev server
python -m pytest                   # Run tests
```


---

## 📂 Project Structure

> **Legend:** `file.ts ← A.tsx, B.tsx` = This file is **imported by** A.tsx and B.tsx.
> Changing this file will affect those files.
>
> ⚠️ **Note:** If a file has no ← annotation but you see imports in the actual code, this dependency is not yet tracked or is incomplete in CODEBASE.md.

```
CODEBASE.md
Dockerfile
LICENSE
README.md
backend/
  __init__.py
  app.py
  babel.cfg
  config.py
  generators/
    __init__.py
    base.py
    factory.py
    google_genai.py
    image_api.py
    openai_compatible.py
  i18n/
    __init__.py
  prompts/
    en_US/
    zh_CN/
      content_prompt.txt
      image_prompt.txt
      image_prompt_short.txt
      outline_prompt.txt
    zh_TW/
  routes/
    __init__.py
    config_routes.py
    content_routes.py
    history_routes.py
    image_routes.py
    outline_routes.py
    utils.py
  services/
    __init__.py
    content.py
    history.py
    image.py
    outline.py
  utils/
    __init__.py
    genai_client.py
    image_compressor.py
    text_client.py
backendpromptsen_US/
backendpromptszh_CN/
backendpromptszh_TW/
docker/
  image_providers.yaml
  text_providers.yaml
docker-compose.yml
frontend/
  index.html
  package-lock.json
  package.json
  pnpm-lock.yaml
  public/
    assets/
      avatars/
        user_avatar.webp
      showcase/
        cover_art.webp
        cover_baby.webp
        cover_baking.webp
        cover_beauty.webp
        cover_books.webp
        cover_camping.webp
        cover_career.webp
        cover_cars.webp
        cover_coffee.webp
        cover_digital_nomad.webp
        cover_diy.webp
        cover_drinks.webp
        cover_education.webp
        cover_english.webp
        cover_fashion.webp
        cover_finance.webp
        cover_fitness.webp
        cover_food.webp
        cover_gaming.webp
        cover_hairstyle.webp
        cover_hiking.webp
        cover_home_cooking.webp
        cover_home_decor.webp
        cover_jewelry.webp
        cover_minimalist.webp
        cover_movies.webp
        cover_music.webp
        cover_nails.webp
        cover_office.webp
        cover_outdoor.webp
        cover_parenting.webp
        cover_pets.webp
        cover_photography.webp
        cover_plants.webp
        cover_psychology.webp
        cover_real_estate.webp
        cover_skincare.webp
        cover_stationery.webp
        cover_tech.webp
        cover_travel.webp
        cover_watches.webp
        cover_wedding.webp
        cover_yoga.webp
      showcase_manifest.json
    logo-banner.png
    logo.png
    showcase1.png
  src/
    App.vue ← main.ts
    api/
      index.ts ← app.py, config_routes.py, image.py
    assets/
      css/
        base.css
        components.css
        history.css
        home.css
        variables.css
    components/
      LanguageSwitcher.vue ← App.vue
      history/
        GalleryCard.vue ← HistoryView.vue
        ImageGalleryModal.vue ← HistoryView.vue
        OutlineModal.vue ← HistoryView.vue
        StatsOverview.vue ← HistoryView.vue
      home/
        ComposerInput.vue ← HomeView.vue
        ShowcaseBackground.vue ← HomeView.vue
      result/
        ContentDisplay.vue ← ResultView.vue
      settings/
        ImageProviderModal.vue ← SettingsView.vue
        ProviderModal.vue ← SettingsView.vue
        ProviderTable.vue ← SettingsView.vue
    composables/
      useProviderForm.ts ← SettingsView.vue
    i18n/
      index.ts ← app.py, config_routes.py, image.py
      locales/
        en-US.ts ← index.ts
        zh-CN.ts ← index.ts
        zh-TW.ts ← index.ts
    main.ts
    router/
      index.ts ← app.py, config_routes.py, image.py
    stores/
      generator.ts ← App.vue, GenerateView.vue, HistoryView.vue +4 more
    views/
      GenerateView.vue ← index.ts
      HistoryView.vue ← index.ts
      HomeView.vue ← index.ts
      OutlineView.vue ← index.ts
      ResultView.vue ← index.ts
      SettingsView.vue ← index.ts
  tsconfig.json
  tsconfig.node.json
  vite.config.ts
history/
image_providers.yaml.example
images/
  1.png
  2.png
  3.png
  coffee.jpg
  example-1.png
  example-2.png
  example-3.png
  example-4.png
  index.gif
  index.png
  logo.png
  redink.png
  showcase-grid.png
nul
pyproject.toml
scripts/
  start-linux.sh
  start-macos.command
  start-windows.bat
start.bat
start.sh
tests/
  __init__.py
  conftest.py
text_providers.yaml.example
uv.lock
```


## 📊 File Dependencies

> Scanned 56 files

### API Endpoints Used

```
/assets/showcase_manifest.json
```

### High-Impact Files

*Files imported by multiple other files:*

| File | Imported by |
|------|-------------|
| `frontend/src/api` | 8 files |
| `backend/i18n` | 8 files |
| `frontend/src/stores/generator` | 7 files |
| `base64` | 7 files |
| `yaml` | 4 files |



---

*This file is auto-generated by Maestro session hooks. Do not edit manually.*
