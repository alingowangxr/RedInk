import { createI18n } from 'vue-i18n'
import enUS from './locales/en-US'
import zhCN from './locales/zh-CN'
import zhTW from './locales/zh-TW'

// 支持的语言列表
export const SUPPORTED_LOCALES = ['en-US', 'zh-CN', 'zh-TW'] as const
export type SupportedLocale = typeof SUPPORTED_LOCALES[number]

// 语言显示名称映射
export const LOCALE_NAMES: Record<SupportedLocale, string> = {
  'en-US': 'English',
  'zh-CN': '简体中文',
  'zh-TW': '繁體中文',
}

// localStorage 键名
const LOCALE_STORAGE_KEY = 'redink-locale'

/**
 * 检测浏览器语言偏好
 */
function detectBrowserLocale(): SupportedLocale {
  const browserLang = navigator.language || (navigator.languages && navigator.languages[0]) || 'zh-CN'

  // 精确匹配
  if (SUPPORTED_LOCALES.includes(browserLang as SupportedLocale)) {
    return browserLang as SupportedLocale
  }

  // 匹配语言前缀（如 en, zh）
  const langPrefix = browserLang.split('-')[0]
  const match = SUPPORTED_LOCALES.find(locale => locale.startsWith(langPrefix))

  return match || 'zh-CN' // 默认简体中文
}

/**
 * 获取初始语言
 * 优先级：localStorage > 浏览器语言 > 默认值
 */
function getInitialLocale(): SupportedLocale {
  const savedLocale = localStorage.getItem(LOCALE_STORAGE_KEY) as SupportedLocale

  if (savedLocale && SUPPORTED_LOCALES.includes(savedLocale)) {
    return savedLocale
  }

  return detectBrowserLocale()
}

// 创建 i18n 实例
const i18n = createI18n({
  legacy: false, // 使用 Composition API 模式
  locale: getInitialLocale(),
  fallbackLocale: 'zh-CN',
  messages: {
    'en-US': enUS,
    'zh-CN': zhCN,
    'zh-TW': zhTW,
  },
  globalInjection: true, // 全局注入 $t
  missingWarn: false, // 生产环境关闭警告
  fallbackWarn: false,
})

/**
 * 切换语言
 */
export function setLocale(locale: SupportedLocale) {
  if (!SUPPORTED_LOCALES.includes(locale)) {
    console.error(`不支持的语言: ${locale}`)
    return
  }

  i18n.global.locale.value = locale
  localStorage.setItem(LOCALE_STORAGE_KEY, locale)

  // 更新 HTML lang 属性
  document.documentElement.lang = locale
}

/**
 * 获取当前语言
 */
export function getCurrentLocale(): SupportedLocale {
  return i18n.global.locale.value as SupportedLocale
}

export default i18n
