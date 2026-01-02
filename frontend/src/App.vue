<template>
  <div id="app">
    <!-- 侧边栏 Sidebar -->
    <aside class="layout-sidebar">
      <div class="logo-area">
        <img src="/logo-banner.png" :alt="t('common.logoAlt')" class="logo-icon" />
      </div>
      
      <nav class="nav-menu">
        <RouterLink to="/" class="nav-item" active-class="active">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
          {{ t('nav.home') }}
        </RouterLink>
        <RouterLink to="/history" class="nav-item" active-class="active">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
          {{ t('nav.history') }}
        </RouterLink>
        <RouterLink to="/settings" class="nav-item" active-class="active">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"></circle><path d="M12 1v6m0 6v6m-6-6h6m6 0h-6"></path><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>
          {{ t('nav.settings') }}
        </RouterLink>
      </nav>

      <div style="margin-top: auto; padding: 16px 20px; display: flex; flex-direction: column; gap: 16px; border-top: 1px solid var(--border-color);">
        <!-- 语言切换器 -->
        <LanguageSwitcher />

        <!-- 用户信息 -->
        <div style="display: flex; align-items: center; gap: 10px;">
          <div style="width: 36px; height: 36px; border-radius: 50%; background: linear-gradient(135deg, var(--primary) 0%, #ff6b6b 100%); display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 14px;">墨</div>
          <div>
            <div style="font-size: 14px; font-weight: 600;">默子</div>
            <div style="font-size: 12px; color: var(--text-sub);">mozi</div>
          </div>
        </div>
      </div>
    </aside>

    <!-- 主内容区 -->
    <main class="layout-main">
      <RouterView v-slot="{ Component, route }">
        <component :is="Component" />

        <!-- 全局页脚版权信息（首页除外） -->
        <footer v-if="route.path !== '/'" class="global-footer">
          <div class="footer-content">
            <div class="footer-tip">
              {{ t('footer.tip') }} <a href="https://redink.top" target="_blank" rel="noopener noreferrer">redink.top</a> {{ t('footer.tipLink') }}
            </div>
            <div class="footer-text">
              {{ t('footer.copyright') }}
            </div>
            <div class="footer-license">
              {{ t('footer.license') }} <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="noopener noreferrer">CC BY-NC-SA 4.0</a>
            </div>
          </div>
        </footer>
      </RouterView>
    </main>
  </div>
</template>

<script setup lang="ts">
import { RouterView, RouterLink } from 'vue-router'
import { onMounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { setupAutoSave } from './stores/generator'
import LanguageSwitcher from './components/LanguageSwitcher.vue'

const { t } = useI18n()

// 启用自动保存到 localStorage
onMounted(() => {
  setupAutoSave()
})
</script>

<style scoped>
/* 布局容器 */
#app {
  display: flex;
  height: 100vh;
  overflow: hidden;
}

/* 侧边栏 */
.layout-sidebar {
  width: 240px;
  background: white;
  border-right: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  padding: 20px;
}

/* Logo 区域 */
.logo-area {
  margin-bottom: 20px;
}

.logo-icon {
  width: 100%;
  height: auto;
  max-height: 40px;
  object-fit: contain;
}

/* 导航菜单 */
.nav-menu {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 20px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  border-radius: 8px;
  color: var(--text-main);
  text-decoration: none;
  transition: all 0.2s;
  font-weight: 500;
}

.nav-item:hover {
  background: rgba(255, 36, 66, 0.05);
  color: var(--primary);
}

.nav-item.active {
  background: rgba(255, 36, 66, 0.1);
  color: var(--primary);
  font-weight: 600;
}

/* 主内容区 */
.layout-main {
  flex: 1;
  overflow-y: auto;
  background: #fafafa;
  position: relative;
}

/* 全局页脚 */
.global-footer {
  padding: 20px;
  text-align: center;
  border-top: 1px solid var(--border-color);
  background: white;
}

.footer-content {
  max-width: 600px;
  margin: 0 auto;
}

.footer-tip {
  font-size: 12px;
  color: var(--text-sub);
  margin-bottom: 8px;
}

.footer-tip a {
  color: var(--primary);
  text-decoration: none;
}

.footer-text {
  font-size: 11px;
  color: var(--text-tertiary);
  margin-bottom: 6px;
}

.footer-license {
  font-size: 11px;
  color: var(--text-tertiary);
}

.footer-license a {
  color: var(--text-secondary);
  text-decoration: none;
}

/* 响应式 */
@media (max-width: 768px) {
  .layout-sidebar {
    width: 60px;
    padding: 12px;
  }

  .logo-area {
    display: none;
  }

  .nav-item span {
    display: none;
  }

  .nav-item {
    justify-content: center;
    padding: 12px;
  }

  .nav-item svg {
    margin-right: 0;
  }
}
</style>

