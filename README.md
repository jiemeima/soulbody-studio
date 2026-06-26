# 灵躯工纺工作室 · 官方网站

> 义乌灵躯工纺工作室官方网站 — 机器人针织服饰（针织仿生软皮肤）定制专家

## 🏢 关于

- **品牌名**：灵躯工纺工作室 / SOULBODY STUDIO
- **母公司**：义乌盈云科技有限公司
- **主营业务**：机器人针织服饰 · 针织仿生软皮肤（Roboskin）设计、定制、量产
- **核心设备**：意大利圣东尼（Santoni）无缝小圆机

## 🌐 部署信息

- **托管平台**：Cloudflare Pages
- **临时域名**：`yingyun-website.pages.dev`（部署后自动分配）
- **生产部署**：每次 push 到 `main` 分支自动部署

## 📁 项目结构

```
企业网站/
├── index.html         # 首页
├── products.html      # 产品中心
├── about.html         # 关于我们
├── contact.html       # 联系我们
├── css/
│   └── style.css      # 全站样式
├── js/
│   └── main.js        # 交互脚本
├── images/            # 图片资源
│   ├── products/      # 产品图
│   └── ...            # 其他图片
├── .gitignore
└── README.md
```

## 🛠 本地开发

```bash
# 启动本地服务器
python -m http.server 8000

# 浏览器访问
http://127.0.0.1:8000
```

## 🚀 部署流程

1. **首次部署**（一次性）
   - 在 Cloudflare Dashboard → Workers & Pages → Create → Pages
   - 连接 GitHub 仓库
   - 配置：
     - Build command: 留空
     - Build output directory: `/`
   - 点击 Save and Deploy
   - 1-2 分钟后获得 `*.pages.dev` 临时域名

2. **更新部署**（之后每次）
   ```bash
   git add .
   git commit -m "更新说明"
   git push
   # Cloudflare 自动部署，约 30 秒
   ```

## 🔍 SEO 配置

部署完成后需做：
- [ ] 百度站长平台收录（https://ziyuan.baidu.com）
- [ ] Google Search Console 收录
- [ ] 提交 sitemap.xml
- [ ] 接入百度统计 / Google Analytics

## 📞 联系方式

- **电话**：13600595031
- **邮箱**：sunny.xu@yingyun-link.com
- **地址**：义乌市川塘路66号盈云科创大厦A栋

---

*© 义乌盈云科技有限公司 | 灵躯工纺工作室*
