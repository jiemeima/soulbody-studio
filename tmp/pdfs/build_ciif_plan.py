from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, NextPageTemplate
)
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from pathlib import Path

ROOT = Path(r"C:\Users\Administrator\Desktop\企业网站")
OUT = ROOT / "output" / "pdf" / "2026中国工博会机器人展参展策划书.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)

pdfmetrics.registerFont(TTFont("CN", r"C:\Windows\Fonts\msyh.ttc"))
pdfmetrics.registerFont(TTFont("CN-Bold", r"C:\Windows\Fonts\msyhbd.ttc"))

NAVY = HexColor("#07141F")
PANEL = HexColor("#102532")
CYAN = HexColor("#19C3D2")
GOLD = HexColor("#C7A35B")
INK = HexColor("#15232C")
MUTED = HexColor("#667780")
PALE = HexColor("#EAF5F6")
LINE = HexColor("#D6E1E5")
WHITE = colors.white

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CNBody", fontName="CN", fontSize=9.2, leading=15, textColor=INK, spaceAfter=5))
styles.add(ParagraphStyle(name="Small", fontName="CN", fontSize=7.5, leading=11, textColor=MUTED))
styles.add(ParagraphStyle(name="H1CN", fontName="CN-Bold", fontSize=20, leading=27, textColor=NAVY, spaceAfter=10))
styles.add(ParagraphStyle(name="H2CN", fontName="CN-Bold", fontSize=13, leading=18, textColor=NAVY, spaceBefore=7, spaceAfter=7))
styles.add(ParagraphStyle(name="H3CN", fontName="CN-Bold", fontSize=10, leading=14, textColor=INK, spaceBefore=5, spaceAfter=3))
styles.add(ParagraphStyle(name="CoverTitle", fontName="CN-Bold", fontSize=27, leading=38, textColor=WHITE, alignment=TA_LEFT))
styles.add(ParagraphStyle(name="CoverSub", fontName="CN", fontSize=11, leading=18, textColor=HexColor("#BFD4DD")))
styles.add(ParagraphStyle(name="Cell", fontName="CN", fontSize=7.5, leading=11, textColor=INK))
styles.add(ParagraphStyle(name="CellBold", fontName="CN-Bold", fontSize=7.5, leading=11, textColor=NAVY))
styles.add(ParagraphStyle(name="CellHead", fontName="CN-Bold", fontSize=7.5, leading=11, textColor=WHITE))
styles.add(ParagraphStyle(name="Quote", fontName="CN-Bold", fontSize=15, leading=24, textColor=NAVY, alignment=TA_CENTER))

def P(text, style="CNBody"):
    return Paragraph(text, styles[style])

def check(text):
    return P("□ " + text)

def header_footer(c, doc):
    c.saveState()
    w, h = A4
    c.setStrokeColor(LINE)
    c.line(18*mm, 15*mm, w-18*mm, 15*mm)
    c.setFont("CN", 7)
    c.setFillColor(MUTED)
    c.drawString(18*mm, 9*mm, "SOULBODY STUDIO · 2026 CIIF RS 参展执行策划")
    c.drawRightString(w-18*mm, 9*mm, f"{doc.page}")
    c.restoreState()

def cover(c, doc):
    w, h = A4
    c.saveState()
    c.setFillColor(NAVY); c.rect(0, 0, w, h, fill=1, stroke=0)
    c.setFillColor(PANEL); c.circle(w*0.92, h*0.73, 74*mm, fill=1, stroke=0)
    c.setStrokeColor(CYAN); c.setLineWidth(0.7)
    for i in range(8):
        y = h*0.18 + i*12*mm
        c.line(w*0.55, y, w*0.92, y+34*mm)
    c.setFillColor(CYAN); c.rect(18*mm, h-40*mm, 18*mm, 2*mm, fill=1, stroke=0)
    c.setFont("CN", 9); c.setFillColor(HexColor("#9EB5BF"))
    c.drawString(18*mm, h-50*mm, "SOULBODY STUDIO / ROBOSKIN")
    c.setFont("CN-Bold", 27); c.setFillColor(WHITE)
    c.drawString(18*mm, h-87*mm, "2026 中国工博会")
    c.drawString(18*mm, h-101*mm, "机器人展参展策划书")
    c.setFont("CN", 12); c.setFillColor(HexColor("#BFD4DD"))
    c.drawString(18*mm, h-118*mm, "为机器人织造第二层皮肤")
    c.setFillColor(GOLD); c.roundRect(18*mm, h-151*mm, 88*mm, 12*mm, 2*mm, fill=1, stroke=0)
    c.setFont("CN-Bold", 9); c.setFillColor(NAVY)
    c.drawCentredString(62*mm, h-147*mm, "2026.10.12 - 10.16 · 上海")
    c.setFont("CN", 8); c.setFillColor(HexColor("#839DA8"))
    c.drawString(18*mm, 25*mm, "规划周期：2026年7月1日 - 10月31日")
    c.drawRightString(w-18*mm, 25*mm, "版本 1.0 · 2026年7月")
    c.restoreState()

doc = BaseDocTemplate(str(OUT), pagesize=A4, leftMargin=18*mm, rightMargin=18*mm,
                      topMargin=18*mm, bottomMargin=20*mm, title="2026中国工博会机器人展参展策划书")
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body")
doc.addPageTemplates([
    PageTemplate(id="cover", frames=frame, onPage=cover),
    PageTemplate(id="normal", frames=frame, onPage=header_footer),
])

story = [NextPageTemplate("normal"), PageBreak()]

story += [P("01 / 项目总览", "H1CN")]
overview = [
    [P("展会", "CellBold"), P("2026中国国际工业博览会 · 机器人展", "Cell")],
    [P("时间", "CellBold"), P("2026年10月12日 - 16日", "Cell")],
    [P("地点", "CellBold"), P("国家会展中心（上海）7.1H、8.1H", "Cell")],
    [P("重点专区", "CellBold"), P("人形机器人、智能养老服务机器人", "Cell")],
    [P("参展定位", "CellBold"), P("Roboskin - 面向人形机器人的针织软皮肤解决方案", "Cell")],
    [P("建议展位", "CellBold"), P("18㎡双开口；优先人形机器人专区或主通道", "Cell")],
]
t = Table(overview, colWidths=[35*mm, 135*mm])
t.setStyle(TableStyle([("BACKGROUND",(0,0),(0,-1),PALE),("GRID",(0,0),(-1,-1),0.4,LINE),
                       ("VALIGN",(0,0),(-1,-1),"MIDDLE"),("LEFTPADDING",(0,0),(-1,-1),7),
                       ("RIGHTPADDING",(0,0),(-1,-1),7),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)]))
story += [t, Spacer(1,8*mm), P("核心主张", "H2CN"), P("为机器人织造第二层皮肤", "Quote"),
          P("展台必须让专业观众在三秒内看懂：我们提供的不是普通机器人服装，而是基于机器人3D结构开发、支持关节弹性与功能材料集成的软皮肤系统。"),
          P("本次参展目标", "H2CN")]
goals = [[P("指标", "CellHead"), P("建议目标", "CellHead"), P("衡量口径", "CellHead")],
         [P("重点预约", "Cell"), P("30家", "Cell"), P("机器人整机厂、创新中心、研究院", "Cell")],
         [P("有效线索", "Cell"), P("150条", "Cell"), P("完成需求字段登记", "Cell")],
         [P("明确打样", "Cell"), P("30个", "Cell"), P("有部位、功能和时间要求", "Cell")],
         [P("展后推进", "Cell"), P("8-10个", "Cell"), P("进入技术评估或报价阶段", "Cell")],
         [P("年度客户", "Cell"), P("2-3家", "Cell"), P("形成连续打样或批量合作", "Cell")]]
t=Table(goals,colWidths=[40*mm,35*mm,95*mm],repeatRows=1)
t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),NAVY),("TEXTCOLOR",(0,0),(-1,0),WHITE),
                       ("GRID",(0,0),(-1,-1),0.4,LINE),("VALIGN",(0,0),(-1,-1),"MIDDLE"),
                       ("ROWBACKGROUNDS",(0,1),(-1,-1),[WHITE,HexColor("#F6F9FA")]),
                       ("LEFTPADDING",(0,0),(-1,-1),6),("RIGHTPADDING",(0,0),(-1,-1),6),
                       ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6)]))
story += [t, PageBreak()]

story += [P("02 / 103天倒计时总表", "H1CN")]
phases = [
    ("P0", "7月1-5日", "报名锁位", "确认展位、签约条件、报馆节点"),
    ("P1", "7月6-15日", "方案确定", "定位、展台、主展品、预算定稿"),
    ("P2", "7月16-31日", "核心展品", "完整软皮肤与功能样件成型"),
    ("P3", "8月1-15日", "技术内容", "参数、视频、折页、需求表"),
    ("P4", "8月16-31日", "设计报审", "施工图、用电、消防、证件"),
    ("P5", "9月1-15日", "客户邀约", "目标名单与一对一预约"),
    ("P6", "9月16-30日", "全面验收", "样品、物料、人员演练"),
    ("P7", "10月1-11日", "物流布展", "发货、进馆、现场联调"),
    ("P8", "10月12-16日", "展会执行", "获客、记录、当日跟进"),
    ("P9", "10月17-31日", "销售转化", "技术会议、报价、打样"),
]
data=[[P("阶段","CellHead"),P("时间","CellHead"),P("主题","CellHead"),P("阶段交付物","CellHead")]]
for a,b,c,d in phases: data.append([P(a,"CellBold"),P(b,"Cell"),P(c,"CellBold"),P(d,"Cell")])
t=Table(data,colWidths=[18*mm,34*mm,35*mm,83*mm],repeatRows=1)
t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),NAVY),("TEXTCOLOR",(0,0),(-1,0),WHITE),
                       ("GRID",(0,0),(-1,-1),0.4,LINE),("VALIGN",(0,0),(-1,-1),"MIDDLE"),
                       ("BACKGROUND",(0,1),(0,-1),PALE),("LEFTPADDING",(0,0),(-1,-1),6),
                       ("RIGHTPADDING",(0,0),(-1,-1),6),("TOPPADDING",(0,0),(-1,-1),7),
                       ("BOTTOMPADDING",(0,0),(-1,-1),7)]))
story += [t, Spacer(1,7*mm), P("三条项目红线", "H2CN"),
          check("7月5日前必须拿到展位图、正式报价和报馆截止日期。"),
          check("7月15日前必须确定展位面积、机器人来源和主展品方案。"),
          check("9月1日起必须进入客户邀约，不能等到展前再开始宣传。"), PageBreak()]

story += [P("03 / P0-P1：报名、锁位与方案", "H1CN"), P("7月1-5日｜报名锁位", "H2CN")]
for x in ["联系主办方，获取2026招展书、展位图、价格表和展商手册。", "确认人形机器人专区剩余展位，比较9㎡、18㎡和36㎡方案。", "优先申请靠近整机企业、主通道或双开口位置。", "确认签约付款、搭建报审、用电、物流、证件和撤展节点。", "申请官方供需对接、新品发布、路演或同期论坛资源。", "提交营业执照、中英文简介、产品图片、知识产权和开票资料。"]: story.append(check(x))
story += [P("官方联系", "H3CN"), P("周女士 021-63811316 / zcm@shanghaiexpogroup.com　　石女士 021-63811737 / lwshi@shanghaiexpogroup.com"),
          P("7月6-15日｜方案确定", "H2CN")]
for x in ["确定参展主题：Roboskin - 为机器人织造第二层皮肤。", "确定目标客户：人形机器人、养老服务机器人、科研及创新中心。", "选择展台搭建公司，提交品牌、尺寸、展品、屏幕和用电需求。", "完成第一版平面布局，预留机器人运动安全区域与储物空间。", "锁定主展机器人来源，并签署借用、运输和保险责任。", "审批总预算、项目负责人和各模块负责人。"]: story.append(check(x))
story += [Spacer(1,4*mm), P("关键决策建议", "H2CN")]
decisions=[[P("事项","CellHead"),P("建议","CellHead")],[P("展位","Cell"),P("18㎡双开口，第一次参展不盲目做36㎡以上","Cell")],[P("陈列","Cell"),P("一台主机器人 + 技术样件墙 + 四人洽谈区","Cell")],[P("视觉","Cell"),P("80%黑白银灰、15%科技青蓝、5%暖金","Cell")],[P("表达","Cell"),P("技术解决方案，不使用传统服装货架逻辑","Cell")]]
t=Table(decisions,colWidths=[35*mm,135*mm]); t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),PANEL),("TEXTCOLOR",(0,0),(-1,0),WHITE),("GRID",(0,0),(-1,-1),0.4,LINE),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("LEFTPADDING",(0,0),(-1,-1),7),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)])); story += [t, PageBreak()]

story += [P("04 / P2-P4：展品、内容与报审", "H1CN"), P("7月16-31日｜核心展品", "H2CN")]
items=["完整Roboskin：穿着于机器人或1:1人形结构模型，另备一套替换件。","肩部微距样件：展示局部贴合和结构成形。","手臂网眼样件：展示透气分区。","肘关节高弹样件：可供观众反复拉伸。","导电纱线/传感器集成样件：证明功能扩展能力。","硬壳、硅胶与针织软皮肤对比样件：解释差异和边界。"]
for x in items: story.append(check(x))
story += [P("8月1-15日｜技术内容", "H2CN")]
for x in ["形成延展率、透气分区、重量、拆洗方式等可公开参数。","明确支持的3D文件格式、打样周期、最小订单和合作流程。","制作30-60秒机器人运动演示视频，并准备离线播放版本。","完成中英文技术折页、名片、样件参数卡和官网专题页。","建立扫码需求表，字段覆盖型号、3D资料、部位、功能、数量和时间。"]: story.append(check(x))
story += [P("8月16-31日｜展台定稿与报审", "H2CN")]
for x in ["完成施工图、效果图、材料说明、用电与网络需求。","提交搭建、消防、展商证、物流车辆及设备进馆资料。","确认进馆、布展、撤展、仓储与垃圾处理规则。","预订住宿交通，购买展品运输保险并锁定物流服务商。"]: story.append(check(x))
story += [PageBreak()]

story += [P("05 / 展台与内容体验方案", "H1CN"), P("推荐18㎡双开口布局", "H2CN")]
layout=[[P("区域","CellHead"),P("内容","CellHead"),P("目的","CellHead")],
        [P("正面主视觉","Cell"),P("完整机器人 + 主标题","Cell"),P("三秒建立品类认知","Cell")],
        [P("左侧样件墙","Cell"),P("肩部、肘部、网眼、导电样件","Cell"),P("让客户触摸并比较","Cell")],
        [P("右侧技术屏","Cell"),P("3D到针织成品流程、参数视频","Cell"),P("建立工程可信度","Cell")],
        [P("后侧洽谈区","Cell"),P("四人桌、资料与隐藏储物","Cell"),P("承接深度沟通","Cell")]]
t=Table(layout,colWidths=[35*mm,78*mm,57*mm],repeatRows=1); t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),NAVY),("TEXTCOLOR",(0,0),(-1,0),WHITE),("GRID",(0,0),(-1,-1),0.4,LINE),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("ROWBACKGROUNDS",(0,1),(-1,-1),[WHITE,HexColor("#F6F9FA")]),("LEFTPADDING",(0,0),(-1,-1),6),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)])); story += [t, Spacer(1,7*mm), P("展墙信息层级", "H2CN")]
for title, body in [("一级","为机器人织造第二层皮肤"),("二级","基于3D结构定制 · 关节弹性分区 · 功能纱线集成"),("三级","需求评估 → 3D数据解析 → 针织算版 → 首版打样 → 测试与量产")]: story += [P(f"<b>{title}</b>　{body}")]
story += [P("互动体验", "H2CN"), check("设置可拉伸样件，让客户直观感受回弹和贴合。"), check("二维码直接进入打样需求表，而非仅跳转企业首页。"), check("技术屏循环播放机器人关节运动及结构标注动画。"), check("所有样件标明用途、结构、材料与可定制内容。"),
          P("避免事项", "H2CN"), P("不摆普通衣架；不使用毛线球或传统纺织意象；不堆叠大段优势文字；不让机器人遮挡品牌名称；不依赖现场网络播放核心视频。"), PageBreak()]

story += [P("06 / P5：客户邀约与传播", "H1CN"), P("目标名单结构", "H2CN")]
targets=[[P("客户类型","CellHead"),P("建议数量","CellHead"),P("重点岗位","CellHead")],
         [P("人形机器人整机厂","Cell"),P("50家","Cell"),P("结构研发、产品、供应链","Cell")],
         [P("服务/养老机器人","Cell"),P("30家","Cell"),P("产品负责人、研发负责人","Cell")],
         [P("创新中心/研究院","Cell"),P("20家","Cell"),P("实验室主任、项目负责人","Cell")],
         [P("集成商/材料伙伴","Cell"),P("30家","Cell"),P("技术合作、商务拓展","Cell")],
         [P("高校及媒体","Cell"),P("20家","Cell"),P("课题组、产业记者","Cell")]]
t=Table(targets,colWidths=[55*mm,30*mm,85*mm],repeatRows=1); t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),NAVY),("TEXTCOLOR",(0,0),(-1,0),WHITE),("GRID",(0,0),(-1,-1),0.4,LINE),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("LEFTPADDING",(0,0),(-1,-1),6),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)])); story += [t, Spacer(1,6*mm)]
for x in ["9月1日前建立150家目标名单，明确联系人、岗位和联系方式。","向重点客户发送一页式技术资料和展位预约链接。","每天安排6-8个预约时段，优先锁定研发与供应链负责人。","9月下旬二次确认；开展前3天发送展位号、地图和联系人。","申请官方供需对接活动，并准备三分钟项目介绍。"]: story.append(check(x))
story += [P("推荐邀约话术", "H2CN"), P("我们提供基于机器人3D结构开发的针织软皮肤，可实现关节弹性、透气分区、可拆洗结构及功能纱线集成。我们将在中国工博会机器人展展示完整样机和结构样件，希望预约20分钟，结合贵司机器人结构评估可行的软皮肤方案。"),
          P("内容发布节奏", "H2CN"), P("9月上旬发布参展预告；9月中旬发布技术样件；9月下旬发布机器人演示；展前一周发布展位地图；展期每天发布现场技术内容。"), PageBreak()]

story += [P("07 / P6-P8：验收、物流与现场", "H1CN"), P("9月16-30日｜全面验收", "H2CN")]
for x in ["机器人连续运行不少于4小时，检查滑移、拉扯与破损。","全部画面和技术资料完成中英文校对。","准备备件、维修工具、离线视频、双份U盘和移动电源。","进行完整接待演练，形成15秒、1分钟、5分钟讲解版本。"]: story.append(check(x))
story += [P("10月1-11日｜发货与布展", "H2CN")]
for x in ["按箱编号并制作装箱清单；关键样件由人员随身携带。","核对机器人及电池运输要求，提前确认进馆车辆和卸货预约。","现场完成灯光、屏幕、网络、二维码和机器人联调。","拍摄布展完成照片，并向预约客户发送最终定位。"]: story.append(check(x))
story += [P("10月12-16日｜人员配置", "H2CN")]
staff=[[P("角色","CellHead"),P("主要职责","CellHead")],[P("技术负责人","Cell"),P("参数、结构、3D资料和打样可行性判断","Cell")],[P("商务负责人","Cell"),P("客户背景、合作模式、价格与下一步推进","Cell")],[P("接待运营","Cell"),P("引流、扫码登记、拍摄和预约秩序","Cell")]]
t=Table(staff,colWidths=[40*mm,130*mm]); t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),PANEL),("TEXTCOLOR",(0,0),(-1,0),WHITE),("GRID",(0,0),(-1,-1),0.4,LINE),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("LEFTPADDING",(0,0),(-1,-1),7),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)])); story += [t, Spacer(1,6*mm)]
for x in ["所有客户必须扫码或登记，并标记A/B/C级。","记录机器人型号、3D资料、覆盖部位、功能、数量和目标时间。","A级客户现场约定下一步，当晚发送资料。","每天闭馆后复盘线索数量、预约到访率和问题反馈。"]: story.append(check(x))
story += [PageBreak()]

story += [P("08 / 预算、风险与责任", "H1CN"), P("预算结构建议", "H2CN")]
budget=[[P("项目","CellHead"),P("建议占比","CellHead"),P("控制原则","CellHead")],
        [P("展位费","Cell"),P("25%-30%","Cell"),P("位置优先于盲目扩面积","Cell")],
        [P("设计搭建","Cell"),P("25%-30%","Cell"),P("突出样机与材料，避免复杂造型","Cell")],
        [P("样品与机器人","Cell"),P("15%-20%","Cell"),P("优先投入可验证的核心展品","Cell")],
        [P("差旅物流","Cell"),P("10%-15%","Cell"),P("提前预订并考虑电池运输","Cell")],
        [P("宣传与客户活动","Cell"),P("10%-15%","Cell"),P("重点投入邀约和技术内容","Cell")],
        [P("应急预留","Cell"),P("10%","Cell"),P("用于返工、加电和临时物流","Cell")]]
t=Table(budget,colWidths=[45*mm,35*mm,90*mm],repeatRows=1); t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),NAVY),("TEXTCOLOR",(0,0),(-1,0),WHITE),("GRID",(0,0),(-1,-1),0.4,LINE),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("LEFTPADDING",(0,0),(-1,-1),6),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)])); story += [t, Spacer(1,6*mm), P("主要风险与预案", "H2CN")]
risks=[[P("风险","CellHead"),P("预案","CellHead")],[P("主机器人无法到场","Cell"),P("准备1:1结构模型及高质量运动视频","Cell")],[P("软皮肤破损/污染","Cell"),P("备用完整件、局部补片、清洁和维修工具","Cell")],[P("网络不稳定","Cell"),P("全部视频、表单演示和资料准备离线版本","Cell")],[P("客户多但无效","Cell"),P("统一需求字段，并由商务负责人当场分级","Cell")],[P("报馆延误","Cell"),P("8月底前完成施工、消防、用电和证件提交","Cell")]]
t=Table(risks,colWidths=[48*mm,122*mm]); t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),PANEL),("TEXTCOLOR",(0,0),(-1,0),WHITE),("GRID",(0,0),(-1,-1),0.4,LINE),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("LEFTPADDING",(0,0),(-1,-1),7),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)])); story += [t, PageBreak()]

story += [P("09 / 展后30天转化计划", "H1CN"), P("展后48小时", "H2CN")]
for x in ["向全部有效客户发送感谢信息和对应资料。","A级客户发送针对性方案，约定线上技术会议。","邀请客户提供机器人3D资料、照片和目标功能。"]: story.append(check(x))
story += [P("展后7天", "H2CN")]
for x in ["完成重点需求技术评估，给出打样周期、费用和资料清单。","建立每个项目的负责人、下一步动作和截止时间。","发布展会复盘内容，继续承接未到场客户。"]: story.append(check(x))
story += [P("展后30天", "H2CN")]
for x in ["统计预约到访、有效线索、打样项目、报价和成交金额。","复盘客户最关注的部位、功能、材料及价格区间。","形成下一阶段产品研发和客户跟进优先级。","评估下一届展位面积、展品结构与投资回报。"]: story.append(check(x))
story += [Spacer(1,8*mm), P("A级线索判定", "H2CN")]
lead=[[P("字段","CellHead"),P("判断标准","CellHead")],[P("项目真实性","Cell"),P("有明确机器人型号或正在研发的本体项目","Cell")],[P("资料条件","Cell"),P("可以提供3D模型、尺寸或实物配合","Cell")],[P("需求明确度","Cell"),P("有覆盖部位、功能、数量和时间要求","Cell")],[P("推进能力","Cell"),P("能够触达技术、采购或项目决策者","Cell")]]
t=Table(lead,colWidths=[45*mm,125*mm]); t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),NAVY),("TEXTCOLOR",(0,0),(-1,0),WHITE),("GRID",(0,0),(-1,-1),0.4,LINE),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("LEFTPADDING",(0,0),(-1,-1),7),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)])); story += [t, Spacer(1,9*mm), P("项目启动结论", "H2CN"), P("当前准备周期充足。立即启动的前三项工作是：锁定人形机器人专区展位、确定18㎡或9㎡方案、确认主展机器人来源。三项决策应在7月15日前全部关闭。")]

doc.build(story)
print(OUT)
