/**
 * 义乌盈云科技有限公司 - 网站主脚本
 * 品牌：YUNSEAM盈云
 */

document.addEventListener('DOMContentLoaded', function() {
  const isEnglish = document.documentElement.lang.toLowerCase().startsWith('en');
  const languagePages = {
    'index.html': 'index-en.html', 'products-roboskin.html': 'products-roboskin-en.html',
    'solutions-humanoid.html': 'solutions-humanoid-en.html', 'products.html': 'products-en.html',
    'about.html': 'about-en.html', 'contact.html': 'contact-en.html', 'faq.html': 'faq-en.html',
    'index-en.html': 'index.html', 'products-roboskin-en.html': 'products-roboskin.html',
    'solutions-humanoid-en.html': 'solutions-humanoid.html', 'products-en.html': 'products.html',
    'about-en.html': 'about.html', 'contact-en.html': 'contact.html', 'faq-en.html': 'faq.html'
  };
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  const navContainer = document.querySelector('.nav-container');
  if (navContainer && languagePages[currentPage]) {
    const languageSwitch = document.createElement('a');
    languageSwitch.className = 'language-switch';
    languageSwitch.href = languagePages[currentPage] + window.location.search + window.location.hash;
    languageSwitch.lang = isEnglish ? 'zh-CN' : 'en';
    languageSwitch.hreflang = isEnglish ? 'zh-CN' : 'en';
    languageSwitch.setAttribute('aria-label', isEnglish ? 'View this page in Chinese' : '切换到英文版');
    languageSwitch.innerHTML = isEnglish ? '<span>中</span> 中文' : '<span>EN</span> English';
    navContainer.insertBefore(languageSwitch, navContainer.querySelector('.mobile-toggle'));
  }
  // 记录推广来源，后续随咨询需求一并发送
  const query = new URLSearchParams(window.location.search);
  const sourceFields = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'];
  sourceFields.forEach(key => {
    if (query.get(key)) localStorage.setItem('lead_' + key, query.get(key));
  });
  if (!localStorage.getItem('lead_first_page')) {
    localStorage.setItem('lead_first_page', window.location.pathname + window.location.search);
    localStorage.setItem('lead_referrer', document.referrer || '直接访问');
  }

  // 全站固定咨询入口
  const conversionBar = document.createElement('aside');
  conversionBar.className = 'conversion-bar';
  conversionBar.setAttribute('aria-label', isEnglish ? 'Quick enquiry' : '快捷咨询');
  conversionBar.innerHTML = isEnglish
    ? '<span><b>Have robot images or dimensions?</b><small>Request a preliminary fit assessment</small></span><button type="button" class="conversion-wechat" data-conversion="wechat">WeChat</button><button type="button" data-phone-trigger data-conversion="phone">Call</button><a class="conversion-primary" href="contact-en.html#assessment" data-conversion="assessment">Get Assessment</a>'
    : '<span><b>有机器人图片或尺寸？</b><small>可先做免费适配判断</small></span><button type="button" class="conversion-wechat" data-conversion="wechat">微信咨询</button><button type="button" data-phone-trigger data-conversion="phone">电话咨询</button><a class="conversion-primary" href="contact.html#assessment" data-conversion="assessment">获取评估</a>';
  document.body.appendChild(conversionBar);

  const wechatModal = document.createElement('div');
  wechatModal.className = 'wechat-modal';
  wechatModal.setAttribute('aria-hidden', 'true');
  wechatModal.innerHTML = isEnglish
    ? '<div class="wechat-modal-backdrop" data-wechat-close></div><div class="wechat-modal-panel" role="dialog" aria-modal="true" aria-labelledby="wechat-modal-title"><button type="button" class="wechat-modal-close" data-wechat-close aria-label="Close WeChat QR code">×</button><span>WECHAT CONTACT</span><h2 id="wechat-modal-title">Scan to Connect</h2><img src="images/wechat-qr-soulbody.jpg" alt="Soulbody Studio WeChat QR code"><p>Send us robot images, dimensions or 3D files after connecting.</p><small>On mobile, press and hold the QR code to scan.</small></div>'
    : '<div class="wechat-modal-backdrop" data-wechat-close></div><div class="wechat-modal-panel" role="dialog" aria-modal="true" aria-labelledby="wechat-modal-title"><button type="button" class="wechat-modal-close" data-wechat-close aria-label="关闭微信二维码">×</button><span>WECHAT CONTACT</span><h2 id="wechat-modal-title">微信扫码咨询</h2><img src="images/wechat-qr-soulbody.jpg" alt="灵躯工纺 Soulbody Studio 微信二维码"><p>添加好友后，可直接发送机器人图片、尺寸或三维资料。</p><small>手机访问时可长按二维码识别</small></div>';
  document.body.appendChild(wechatModal);
  const wechatTrigger = conversionBar.querySelector('.conversion-wechat');
  const openWechat = function() {
    wechatModal.classList.add('active');
    wechatModal.setAttribute('aria-hidden', 'false');
    document.body.classList.add('modal-open');
    wechatModal.querySelector('.wechat-modal-close').focus();
  };
  const closeWechat = function() {
    wechatModal.classList.remove('active');
    wechatModal.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('modal-open');
    wechatTrigger.focus();
  };
  wechatTrigger.addEventListener('click', openWechat);
  wechatModal.querySelectorAll('[data-wechat-close]').forEach(el => el.addEventListener('click', closeWechat));
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && wechatModal.classList.contains('active')) closeWechat();
  });

  // 电话咨询：电脑端显示并复制号码，手机端再提供系统拨号入口
  const phoneModal = document.createElement('div');
  phoneModal.className = 'phone-modal';
  phoneModal.setAttribute('aria-hidden', 'true');
  phoneModal.innerHTML = isEnglish
    ? '<div class="phone-modal-backdrop" data-phone-close></div><div class="phone-modal-panel" role="dialog" aria-modal="true" aria-labelledby="phone-modal-title"><button type="button" class="phone-modal-close" data-phone-close aria-label="Close phone enquiry">×</button><span>PHONE CONTACT</span><h2 id="phone-modal-title">Call Us</h2><strong>+86 136 0059 5031</strong><p>Monday-Friday, 8:00-17:30 (China Standard Time)</p><div class="phone-modal-actions"><button type="button" class="phone-copy">Copy Number</button><a href="tel:+8613600595031" class="phone-call">Call Now</a></div><small>International calls are welcome. Email is recommended outside working hours.</small></div>'
    : '<div class="phone-modal-backdrop" data-phone-close></div><div class="phone-modal-panel" role="dialog" aria-modal="true" aria-labelledby="phone-modal-title"><button type="button" class="phone-modal-close" data-phone-close aria-label="关闭电话咨询">×</button><span>PHONE CONTACT</span><h2 id="phone-modal-title">电话咨询</h2><strong>136 0059 5031</strong><p>工作时间：周一至周五 8:00–17:30</p><div class="phone-modal-actions"><button type="button" class="phone-copy">复制号码</button><a href="tel:13600595031" class="phone-call">一键拨号</a></div><small>电脑端请复制号码；手机端可点击一键拨号。</small></div>';
  document.body.appendChild(phoneModal);
  const phoneTriggers = document.querySelectorAll('[data-phone-trigger]');
  const phoneClose = phoneModal.querySelector('.phone-modal-close');
  const openPhone = function() {
    phoneModal.classList.add('active');
    phoneModal.setAttribute('aria-hidden', 'false');
    document.body.classList.add('modal-open');
    phoneClose.focus();
  };
  const closePhone = function() {
    phoneModal.classList.remove('active');
    phoneModal.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('modal-open');
  };
  phoneTriggers.forEach(el => el.addEventListener('click', openPhone));
  phoneModal.querySelectorAll('[data-phone-close]').forEach(el => el.addEventListener('click', closePhone));
  phoneModal.querySelector('.phone-copy').addEventListener('click', async function() {
    try {
      if (navigator.clipboard && window.isSecureContext) await navigator.clipboard.writeText('13600595031');
      else throw new Error('clipboard unavailable');
      this.textContent = isEnglish ? 'Number Copied' : '号码已复制';
    } catch (err) {
      this.textContent = isEnglish ? 'Please copy manually: +86 13600595031' : '请手动复制：13600595031';
    }
  });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && phoneModal.classList.contains('active')) closePhone();
  });
  // 移动端菜单切换
  const mobileToggle = document.querySelector('.mobile-toggle');
  const navMenu = document.querySelector('.nav-menu');
  
  if (mobileToggle) {
    mobileToggle.addEventListener('click', function() {
      navMenu.classList.toggle('active');
    });
  }
  
  // 点击导航链接后关闭移动端菜单
  const navLinks = document.querySelectorAll('.nav-menu a');
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      navMenu.classList.remove('active');
    });
  });
  
  // 导航栏滚动效果
  const navbar = document.querySelector('.navbar');
  let lastScroll = 0;
  
  window.addEventListener('scroll', function() {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 100) {
      navbar.style.boxShadow = '0 2px 20px rgba(0,0,0,0.3)';
    } else {
      navbar.style.boxShadow = 'none';
    }
    
    lastScroll = currentScroll;
  });
  
  // 滚动显示动画
  const revealElements = document.querySelectorAll('.reveal');
  
  const revealOnScroll = function() {
    revealElements.forEach(element => {
      const elementTop = element.getBoundingClientRect().top;
      const windowHeight = window.innerHeight;
      
      if (elementTop < windowHeight - 100) {
        element.classList.add('active');
      }
    });
  };
  
  window.addEventListener('scroll', revealOnScroll);
  revealOnScroll(); // 初始检查
  
  // 平滑滚动到锚点
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
  
  // 静态站需求表单：整理为邮件，同时保留复制兜底
  const leadForm = document.getElementById('lead-form');
  const copyLead = document.getElementById('copy-lead');
  const buildLeadText = function() {
    if (!leadForm) return '';
    const data = new FormData(leadForm);
    const source = sourceFields.map(key => localStorage.getItem('lead_' + key)).filter(Boolean).join(' / ') || '自然访问或未标记';
    return (isEnglish ? [
      'Preliminary Roboskin Project Assessment', '',
      'Company / Organization: ' + (data.get('company') || ''), 'Contact: ' + (data.get('name') || ''),
      'Phone: ' + (data.get('phone') || ''), 'Email: ' + (data.get('email') || 'Not provided'),
      'Robot Type: ' + (data.get('robotType') || ''), 'Estimated Quantity: ' + (data.get('quantity') || ''),
      'Requirements: ' + (data.get('requirements') || ''), '', 'Submitted from: ' + window.location.href
    ] : [
      '机器人软皮肤定制初步评估需求', '', '公司/机构：' + (data.get('company') || ''),
      '联系人：' + (data.get('name') || ''), '联系电话：' + (data.get('phone') || ''),
      '联系邮箱：' + (data.get('email') || '未填写'), '机器人类型：' + (data.get('robotType') || ''),
      '预计数量：' + (data.get('quantity') || ''), '需求说明：' + (data.get('requirements') || ''), '',
      '推广来源：' + source, '首次访问：' + (localStorage.getItem('lead_first_page') || ''),
      '来源页面：' + (localStorage.getItem('lead_referrer') || '直接访问'), '提交页面：' + window.location.href
    ]).join('\n');
  };
  const validateLead = function() {
    const error = leadForm.querySelector('.lead-form-error');
    if (!leadForm.checkValidity()) {
      error.textContent = isEnglish ? 'Please complete the required fields and accept the privacy notice.' : '请完成公司、联系人、电话、机器人类型、需求说明及信息使用同意。';
      leadForm.reportValidity();
      return false;
    }
    error.textContent = '';
    return true;
  };
  if (leadForm) {
    leadForm.addEventListener('submit', function(e) {
      e.preventDefault();
      if (!validateLead()) return;
      const company = new FormData(leadForm).get('company');
      const subject = (isEnglish ? 'Roboskin Project Assessment | ' : '机器人软皮肤定制评估｜') + company;
      window.location.href = 'mailto:sunny.xu@yingyun-link.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(buildLeadText());
    });
  }
  if (copyLead) {
    copyLead.addEventListener('click', async function() {
      if (!validateLead()) return;
      try {
        const leadText = buildLeadText();
        if (navigator.clipboard && window.isSecureContext) {
          await navigator.clipboard.writeText(leadText);
        } else {
          const fallback = document.createElement('textarea');
          fallback.value = leadText;
          fallback.setAttribute('readonly', '');
          fallback.style.position = 'fixed';
          fallback.style.opacity = '0';
          document.body.appendChild(fallback);
          fallback.select();
          const copied = document.execCommand('copy');
          fallback.remove();
          if (!copied) throw new Error('copy unavailable');
        }
        copyLead.textContent = isEnglish ? 'Copied - paste into WeChat or email' : '已复制，可粘贴到微信或邮件';
      } catch (err) {
        copyLead.textContent = isEnglish ? 'Copy unavailable - please use email' : '复制受限，请使用发送邮件';
      }
    });
  }

  // 产品分类筛选（产品页面）— 已隐藏筛选栏后停用
  // const filterButtons = document.querySelectorAll('.filter-btn');
  // const productCards = document.querySelectorAll('.product-card');
  
  // if (filterButtons.length > 0) {
  //   filterButtons.forEach(button => {
  //     button.addEventListener('click', function() {
  //       const filter = this.dataset.filter;
  //       
  //       // 更新按钮状态
  //       filterButtons.forEach(btn => btn.classList.remove('active'));
  //       this.classList.add('active');
  //       
  //       // 筛选产品
  //       productCards.forEach(card => {
  //         if (filter === 'all' || card.dataset.category === filter) {
  //           card.style.removeProperty('display');
  //           setTimeout(() => {
  //             card.style.opacity = '1';
  //             card.style.transform = 'translateY(0)';
  //           }, 50);
  //         } else {
  //           card.style.opacity = '0';
  //           card.style.transform = 'translateY(20px)';
  //           setTimeout(() => {
  //             card.style.display = 'none';
  //           }, 300);
  //         }
  //       });
  //     });
  //   });
  // }
  
  // 数字计数动画
  const statNumbers = document.querySelectorAll('.stat-number');
  
  const animateNumbers = function() {
    statNumbers.forEach(stat => {
      const target = parseInt(stat.dataset.target);
      const numEl = stat.querySelector('.num') || stat;
      const current = parseInt(numEl.textContent);
      const increment = target / 50;
      
      if (current < target) {
        numEl.textContent = Math.ceil(current + increment);
        setTimeout(animateNumbers, 30);
      } else {
        numEl.textContent = target;
      }
    });
  };
  
  // 当统计区域进入视口时开始动画
  const statsSection = document.querySelector('.stats-grid');
  if (statsSection) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateNumbers();
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    
    observer.observe(statsSection);
  }
});

// 页面加载完成后的初始化
window.addEventListener('load', function() {
  document.body.classList.add('loaded');
});
