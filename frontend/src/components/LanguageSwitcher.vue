<template>
  <div class="language-switcher" @click.stop>
    <button
      class="lang-btn"
      :class="{ active: showDropdown }"
      @click="toggleDropdown"
    >
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10"></circle>
        <line x1="2" y1="12" x2="22" y2="12"></line>
        <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
      </svg>
      <span>{{ LOCALE_NAMES[currentLocale] }}</span>
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <polyline points="6 9 12 15 18 9"></polyline>
      </svg>
    </button>

    <div v-if="showDropdown" class="lang-dropdown">
      <div
        v-for="locale in SUPPORTED_LOCALES"
        :key="locale"
        class="lang-option"
        :class="{ active: locale === currentLocale }"
        @click="switchLanguage(locale)"
      >
        {{ LOCALE_NAMES[locale] }}
        <svg v-if="locale === currentLocale" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="20 6 9 17 4 12"></polyline>
        </svg>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { SUPPORTED_LOCALES, LOCALE_NAMES, setLocale, getCurrentLocale, type SupportedLocale } from '../i18n'

const showDropdown = ref(false)
const currentLocale = ref<SupportedLocale>(getCurrentLocale())

function toggleDropdown() {
  showDropdown.value = !showDropdown.value
}

function switchLanguage(newLocale: SupportedLocale) {
  setLocale(newLocale)
  currentLocale.value = newLocale
  showDropdown.value = false
}

// 点击外部关闭下拉菜单
function handleClickOutside(event: MouseEvent) {
  const target = event.target as HTMLElement
  if (!target.closest('.language-switcher')) {
    showDropdown.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<style scoped>
.language-switcher {
  position: relative;
}

.lang-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  background: white;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  cursor: pointer;
  font-size: 14px;
  color: var(--text-main);
  transition: all 0.2s;
}

.lang-btn:hover,
.lang-btn.active {
  border-color: var(--primary);
  color: var(--primary);
}

.lang-dropdown {
  position: absolute;
  top: calc(100% + 4px);
  right: 0;
  background: white;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  min-width: 150px;
  z-index: 1000;
  overflow: hidden;
}

.lang-option {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 16px;
  cursor: pointer;
  font-size: 14px;
  color: var(--text-main);
  transition: background 0.2s;
}

.lang-option:hover {
  background: #f5f5f5;
}

.lang-option.active {
  color: var(--primary);
  font-weight: 600;
  background: rgba(255, 107, 107, 0.05);
}
</style>
