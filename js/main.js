/**
 * 义乌盈云科技有限公司 - 网站主脚本
 * 品牌：YUNSEAM盈云
 */

document.addEventListener('DOMContentLoaded', function() {
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
  
  // 联系表单提交处理—已删除表单后停用
  // const contactForm = document.querySelector('.contact-form form');
  // if (contactForm) {
  //   contactForm.addEventListener('submit', function(e) {
  //     e.preventDefault();
  //     ...
  //   });
  // }

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
