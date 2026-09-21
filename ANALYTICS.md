# 官网统计上报

浏览器通过同域 `/api/website-analytics/events` POST 上报匿名页面浏览和点击。
Pages Function 将请求转发到客户平台的公开统计接口，不转发 Cookie 或授权头。

## 正式接收路径

官网浏览器 → 官网 Pages Function → https://pawpark.com.cn/api/website-analytics/events
→ 客户平台公开统计接口。

Pawpark 使用现有域名、HTTPS 证书及服务器 47.98.231.28。
Nginx 只为该精确路径增加转发，原网站页面继续使用原路由。
保留原始 Origin，因此数据归属 soulbody-studio.com，不归属 Pawpark。
服务器间使用现有客户平台 HTTP 接口，仅转发匿名统计，不转发登录凭证。
原 analytics-origin.soulbody-studio.com 路径因源站备案拦截弃用，无需再依赖该 DNS 记录。

Pawpark 配置：/opt/legendshop/services/nginx/config/legendshopConfig/pawpark-https.conf。
变更前备份：/opt/legendshop/services/nginx/config/pawpark-https.before-analytics-20260921-1701.bak。

## 验证

1. 正式站 `js/main.js` 中上报地址为 `/api/website-analytics/events`。
2. GET 此接口返回 405，POST 页面浏览及点击返回业务成功响应。
3. 客户平台选择 soulbody-studio.com 检查新增统计。

历史中断期间的数据无法补录。遵守浏览器 Do Not Track / Global Privacy Control 设置。
