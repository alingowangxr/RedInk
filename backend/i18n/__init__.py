"""
后端国际化 (i18n) 工具模块

提供功能：
1. 从请求头获取用户语言偏好
2. 翻译错误消息和提示文本
3. 动态加载多语言 AI 提示词模板
"""

import os
from flask import request
from functools import lru_cache

# 支持的语言列表
SUPPORTED_LOCALES = ['zh-CN', 'en-US', 'zh-TW']
DEFAULT_LOCALE = 'zh-CN'

# 语言代码映射（HTTP Accept-Language 格式 ↔ 文件系统格式）
LOCALE_MAP = {
    'zh-CN': 'zh_CN',
    'zh-cn': 'zh_CN',
    'zh': 'zh_CN',
    'en-US': 'en_US',
    'en-us': 'en_US',
    'en': 'en_US',
    'zh-TW': 'zh_TW',
    'zh-tw': 'zh_TW',
    'zh-Hant': 'zh_TW',
}


def get_locale():
    """
    从 Accept-Language 请求头获取用户语言偏好

    Returns:
        str: 语言代码，格式为 'zh-CN', 'en-US', 'zh-TW'
    """
    # 从请求头获取语言
    accept_language = request.headers.get('Accept-Language', DEFAULT_LOCALE)

    # 解析 Accept-Language 头（可能包含多个语言和权重）
    # 例如: "en-US,en;q=0.9,zh-CN;q=0.8"
    if ',' in accept_language:
        # 取第一个语言（权重最高）
        accept_language = accept_language.split(',')[0].strip()

    # 移除权重部分
    if ';' in accept_language:
        accept_language = accept_language.split(';')[0].strip()

    # 标准化语言代码
    if accept_language in SUPPORTED_LOCALES:
        return accept_language

    # 尝试匹配简化的语言代码
    if accept_language.startswith('zh'):
        if 'TW' in accept_language or 'Hant' in accept_language:
            return 'zh-TW'
        return 'zh-CN'
    elif accept_language.startswith('en'):
        return 'en-US'

    return DEFAULT_LOCALE


def to_fs_locale(locale):
    """
    将 HTTP 格式的语言代码转换为文件系统格式

    Args:
        locale: HTTP 格式的语言代码，如 'zh-CN'

    Returns:
        str: 文件系统格式的语言代码，如 'zh_CN'
    """
    return LOCALE_MAP.get(locale, LOCALE_MAP.get(DEFAULT_LOCALE))


@lru_cache(maxsize=128)
def load_prompt_template(template_name, locale=None):
    """
    动态加载多语言 AI 提示词模板

    Args:
        template_name: 模板文件名，如 'outline_prompt.txt'
        locale: 语言代码（可选），如果未指定则从请求头获取

    Returns:
        str: 提示词模板内容

    Raises:
        FileNotFoundError: 如果模板文件不存在
    """
    if locale is None:
        locale = get_locale()

    # 转换为文件系统格式
    fs_locale = to_fs_locale(locale)

    # 构建模板文件路径
    # 目录结构: backend/prompts/{locale}/{template_name}
    backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_path = os.path.join(backend_dir, 'prompts', fs_locale, template_name)

    # 尝试加载模板
    if os.path.exists(template_path):
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()

    # 降级策略：如果指定语言的模板不存在，使用默认语言（中文）
    default_path = os.path.join(backend_dir, 'prompts', 'zh_CN', template_name)
    if os.path.exists(default_path):
        with open(default_path, 'r', encoding='utf-8') as f:
            return f.read()

    raise FileNotFoundError(f"Template {template_name} not found for locale {locale}")


# 简化的翻译系统（不依赖 Flask-Babel）
# 直接使用字典存储翻译
TRANSLATIONS = {
    'en_US': {
        # Outline routes
        'topic_required_detail': 'Parameter error: topic cannot be empty.\nPlease provide the topic for generating images.',
        'outline_exception': 'Outline generation error.\nError details: {error}\nSuggestion: Check backend logs for more information',

        # Content routes
        'topic_required_content': 'Parameter error: topic cannot be empty.\nPlease provide topic content.',
        'outline_required': 'Parameter error: outline cannot be empty.\nPlease generate outline first.',
        'content_exception': 'Content generation error.\nError details: {error}\nSuggestion: Check backend logs for more information',

        # Image routes
        'pages_required': 'Parameter error: pages cannot be empty.\nPlease provide page list data.',
        'image_exception': 'Image generation error.\nError details: {error}\nSuggestion: Check image generation service configuration and backend logs',
        'image_not_found': 'Image not found: {task_id}/{filename}',
        'get_image_failed': 'Failed to get image: {error}',
        'retry_params_required': 'Parameter error: task_id and page cannot be empty.\nPlease provide task ID and page information.',
        'retry_single_failed': 'Failed to retry image generation.\nError details: {error}',
        'retry_batch_params_required': 'Parameter error: task_id and pages cannot be empty.\nPlease provide task ID and page list to retry.',
        'retry_batch_failed': 'Batch retry failed.\nError details: {error}',
        'regenerate_failed': 'Failed to regenerate image.\nError details: {error}',
        'task_not_found_detail': 'Task not found: {task_id}\nPossible reasons:\n1. Incorrect task ID\n2. Task expired or cleaned\n3. Service restart caused state loss',
        'get_task_state_failed': 'Failed to get task state.\nError details: {error}',
        'service_healthy': 'Service is running normally',

        # History routes
        'history_create_params_required': 'Parameter error: topic and outline cannot be empty.\nPlease provide topic and outline content.',
        'history_create_failed': 'Failed to create history record.\nError details: {error}',
        'history_list_failed': 'Failed to get history list.\nError details: {error}',
        'history_not_found_detail': 'History record not found: {record_id}\nPossible reasons: Record deleted or incorrect ID',
        'history_get_failed': 'Failed to get history details.\nError details: {error}',
        'history_check_failed': 'Failed to check record.\nError details: {error}',
        'history_update_not_found': 'Failed to update history: {record_id}\nPossible reasons: Record not found or invalid data format',
        'history_update_failed': 'Failed to update history.\nError details: {error}',
        'history_delete_not_found': 'Failed to delete history: {record_id}\nPossible reasons: Record not found or incorrect ID',
        'history_delete_failed': 'Failed to delete history.\nError details: {error}',
        'keyword_required': 'Parameter error: keyword cannot be empty.\nPlease provide search keyword.',
        'history_search_failed': 'Failed to search history.\nError details: {error}',
        'history_stats_failed': 'Failed to get history statistics.\nError details: {error}',
        'scan_task_failed': 'Failed to scan task.\nError details: {error}',
        'scan_all_failed': 'Failed to scan all tasks.\nError details: {error}',
        'download_no_task': 'This record has no associated task images',
        'task_dir_not_found': 'Task directory not found: {task_id}',
        'download_failed': 'Download failed.\nError details: {error}',

        # Config routes
        'get_config_failed': 'Failed to get configuration: {error}',
        'update_config_failed': 'Failed to update configuration: {error}',
        'config_saved': 'Configuration saved',
        'type_required': 'Missing type parameter',
        'api_key_not_configured': 'API Key not configured',
        'unsupported_type': 'Unsupported type: {provider_type}',
        'connection_success_unstable': 'Connection successful! Only indicates stable connection, stability of image generation not guaranteed',
        'connection_test_failed': 'Connection test failed: {error}',
        'vertex_ai_no_test': 'Vertex AI cannot test connection via API Key (OAuth2 required). Please verify configuration when generating images.',
        'connection_success_response': 'Connection successful! Response: {response}',
        'connection_success_unexpected': 'Connection successful, but response content unexpected: {response}',
    },
    'zh_TW': {
        # Outline routes
        'topic_required_detail': '參數錯誤：topic 不能為空。\n請提供要生成圖文的主題內容。',
        'outline_exception': '大綱生成異常。\n錯誤詳情: {error}\n建議：檢查後端日誌獲取更多資訊',

        # Content routes
        'topic_required_content': '參數錯誤：topic 不能為空。\n請提供主題內容。',
        'outline_required': '參數錯誤：outline 不能為空。\n請先生成大綱。',
        'content_exception': '內容生成異常。\n錯誤詳情: {error}\n建議：檢查後端日誌獲取更多資訊',

        # Image routes
        'pages_required': '參數錯誤：pages 不能為空。\n請提供要生成的頁面列表數據。',
        'image_exception': '圖片生成異常。\n錯誤詳情: {error}\n建議：檢查圖片生成服務配置和後端日誌',
        'image_not_found': '圖片不存在：{task_id}/{filename}',
        'get_image_failed': '獲取圖片失敗: {error}',
        'retry_params_required': '參數錯誤：task_id 和 page 不能為空。\n請提供任務ID和頁面資訊。',
        'retry_single_failed': '重試圖片生成失敗。\n錯誤詳情: {error}',
        'retry_batch_params_required': '參數錯誤：task_id 和 pages 不能為空。\n請提供任務ID和要重試的頁面列表。',
        'retry_batch_failed': '批量重試失敗。\n錯誤詳情: {error}',
        'regenerate_failed': '重新生成圖片失敗。\n錯誤詳情: {error}',
        'task_not_found_detail': '任務不存在：{task_id}\n可能原因：\n1. 任務ID錯誤\n2. 任務已過期或被清理\n3. 服務重啟導致狀態丟失',
        'get_task_state_failed': '獲取任務狀態失敗。\n錯誤詳情: {error}',
        'service_healthy': '服務正常運行',

        # History routes
        'history_create_params_required': '參數錯誤：topic 和 outline 不能為空。\n請提供主題和大綱內容。',
        'history_create_failed': '創建歷史記錄失敗。\n錯誤詳情: {error}',
        'history_list_failed': '獲取歷史記錄列表失敗。\n錯誤詳情: {error}',
        'history_not_found_detail': '歷史記錄不存在：{record_id}\n可能原因：記錄已被刪除或ID錯誤',
        'history_get_failed': '獲取歷史記錄詳情失敗。\n錯誤詳情: {error}',
        'history_check_failed': '檢查記錄失敗。\n錯誤詳情: {error}',
        'history_update_not_found': '更新歷史記錄失敗：{record_id}\n可能原因：記錄不存在或數據格式錯誤',
        'history_update_failed': '更新歷史記錄失敗。\n錯誤詳情: {error}',
        'history_delete_not_found': '刪除歷史記錄失敗：{record_id}\n可能原因：記錄不存在或ID錯誤',
        'history_delete_failed': '刪除歷史記錄失敗。\n錯誤詳情: {error}',
        'keyword_required': '參數錯誤：keyword 不能為空。\n請提供搜尋關鍵詞。',
        'history_search_failed': '搜尋歷史記錄失敗。\n錯誤詳情: {error}',
        'history_stats_failed': '獲取歷史記錄統計失敗。\n錯誤詳情: {error}',
        'scan_task_failed': '掃描任務失敗。\n錯誤詳情: {error}',
        'scan_all_failed': '掃描所有任務失敗。\n錯誤詳情: {error}',
        'download_no_task': '該記錄沒有關聯的任務圖片',
        'task_dir_not_found': '任務目錄不存在：{task_id}',
        'download_failed': '下載失敗。\n錯誤詳情: {error}',

        # Config routes
        'get_config_failed': '獲取配置失敗: {error}',
        'update_config_failed': '更新配置失敗: {error}',
        'config_saved': '配置已保存',
        'type_required': '缺少 type 參數',
        'api_key_not_configured': 'API Key 未配置',
        'unsupported_type': '不支援的類型: {provider_type}',
        'connection_success_unstable': '連線成功！僅代表連線穩定，不確定是否可以穩定支援圖片生成',
        'connection_test_failed': '連線測試失敗: {error}',
        'vertex_ai_no_test': 'Vertex AI 無法透過 API Key 測試連線（需要 OAuth2 認證）。請在實際生成圖片時驗證配置是否正確。',
        'connection_success_response': '連線成功！響應: {response}',
        'connection_success_unexpected': '連線成功，但響應內容不符合預期: {response}',
    },
    'zh_CN': {
        # Outline routes
        'topic_required_detail': '参数错误：topic 不能为空。\n请提供要生成图文的主题内容。',
        'outline_exception': '大纲生成异常。\n错误详情: {error}\n建议：检查后端日志获取更多信息',

        # Content routes
        'topic_required_content': '参数错误：topic 不能为空。\n请提供主题内容。',
        'outline_required': '参数错误：outline 不能为空。\n请先生成大纲。',
        'content_exception': '内容生成异常。\n错误详情: {error}\n建议：检查后端日志获取更多信息',

        # Image routes
        'pages_required': '参数错误：pages 不能为空。\n请提供要生成的页面列表数据。',
        'image_exception': '图片生成异常。\n错误详情: {error}\n建议：检查图片生成服务配置和后端日志',
        'image_not_found': '图片不存在：{task_id}/{filename}',
        'get_image_failed': '获取图片失败: {error}',
        'retry_params_required': '参数错误：task_id 和 page 不能为空。\n请提供任务ID和页面信息。',
        'retry_single_failed': '重试图片生成失败。\n错误详情: {error}',
        'retry_batch_params_required': '参数错误：task_id 和 pages 不能为空。\n请提供任务ID和要重试的页面列表。',
        'retry_batch_failed': '批量重试失败。\n错误详情: {error}',
        'regenerate_failed': '重新生成图片失败。\n错误详情: {error}',
        'task_not_found_detail': '任务不存在：{task_id}\n可能原因：\n1. 任务ID错误\n2. 任务已过期或被清理\n3. 服务重启导致状态丢失',
        'get_task_state_failed': '获取任务状态失败。\n错误详情: {error}',
        'service_healthy': '服务正常运行',

        # History routes
        'history_create_params_required': '参数错误：topic 和 outline 不能为空。\n请提供主题和大纲内容。',
        'history_create_failed': '创建历史记录失败。\n错误详情: {error}',
        'history_list_failed': '获取历史记录列表失败。\n错误详情: {error}',
        'history_not_found_detail': '历史记录不存在：{record_id}\n可能原因：记录已被删除或ID错误',
        'history_get_failed': '获取历史记录详情失败。\n错误详情: {error}',
        'history_check_failed': '检查记录失败。\n错误详情: {error}',
        'history_update_not_found': '更新历史记录失败：{record_id}\n可能原因：记录不存在或数据格式错误',
        'history_update_failed': '更新历史记录失败。\n错误详情: {error}',
        'history_delete_not_found': '删除历史记录失败：{record_id}\n可能原因：记录不存在或ID错误',
        'history_delete_failed': '删除历史记录失败。\n错误详情: {error}',
        'keyword_required': '参数错误：keyword 不能为空。\n请提供搜索关键词。',
        'history_search_failed': '搜索历史记录失败。\n错误详情: {error}',
        'history_stats_failed': '获取历史记录统计失败。\n错误详情: {error}',
        'scan_task_failed': '扫描任务失败。\n错误详情: {error}',
        'scan_all_failed': '扫描所有任务失败。\n错误详情: {error}',
        'download_no_task': '该记录没有关联的任务图片',
        'task_dir_not_found': '任务目录不存在：{task_id}',
        'download_failed': '下载失败。\n错误详情: {error}',

        # Config routes
        'get_config_failed': '获取配置失败: {error}',
        'update_config_failed': '更新配置失败: {error}',
        'config_saved': '配置已保存',
        'type_required': '缺少 type 参数',
        'api_key_not_configured': 'API Key 未配置',
        'unsupported_type': '不支持的类型: {provider_type}',
        'connection_success_unstable': '连接成功！仅代表连接稳定，不确定是否可以稳定支持图片生成',
        'connection_test_failed': '连接测试失败: {error}',
        'vertex_ai_no_test': 'Vertex AI 无法通过 API Key 测试连接（需要 OAuth2 认证）。请在实际生成图片时验证配置是否正确。',
        'connection_success_response': '连接成功！响应: {response}',
        'connection_success_unexpected': '连接成功，但响应内容不符合预期: {response}',
    }
}


def gettext(message_id, locale=None, **kwargs):
    """
    获取翻译文本

    Args:
        message_id: 消息ID
        locale: 语言代码（可选）
        **kwargs: 格式化参数

    Returns:
        str: 翻译后的文本
    """
    if locale is None:
        locale = get_locale()

    fs_locale = to_fs_locale(locale)

    # 从翻译字典获取
    if fs_locale in TRANSLATIONS and message_id in TRANSLATIONS[fs_locale]:
        text = TRANSLATIONS[fs_locale][message_id]
    # 降级到默认语言
    elif message_id in TRANSLATIONS['zh_CN']:
        text = TRANSLATIONS['zh_CN'][message_id]
    else:
        # 如果找不到翻译，返回消息ID本身
        text = message_id

    # 如果有格式化参数，进行格式化
    if kwargs:
        try:
            text = text.format(**kwargs)
        except KeyError:
            # 如果格式化失败，返回原始文本
            pass

    return text


# 简化别名
_ = gettext
