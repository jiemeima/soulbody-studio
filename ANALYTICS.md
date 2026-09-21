# 官网统计上报

浏览器通过同域 `/api/website-analytics/events` POST 上报匿名页面浏览和点击。
Pages Function 将请求转发到客户平台的公开统计接口，不转发 Cookie 或授权头。

## 必需的 DNS 配置

在 soulbody-studio.com 的 Cloudflare DNS 添加：

- 类型：A
- 名称：analytics-origin
- IPv4：120.55.193.185
- 代理状态：仅 DNS（灰色云朵）
- TTL：自动

该域名用于 Pages 服务端访问 15666 端口；浏览器仍只访问官网 HTTPS。
Cloudflare fetch 不支持直接访问 IP，且代理模式不支持这里使用的 15666 端口。
源站目前使用 HTTP，仅传输现有匿名统计字段，不传输登录凭证。
不要更改官网根域名或 www 的解析。

## 验证

1. 正式站 `js/main.js` 中上报地址为 `/api/website-analytics/events`。
2. GET 此接口返回 405，POST 页面浏览及点击返回业务成功响应。
3. 客户平台选择 soulbody-studio.com 检查新增统计。

历史中断期间的数据无法补录。遵守浏览器 Do Not Track / Global Privacy Control 设置。
