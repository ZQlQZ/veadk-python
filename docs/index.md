---
hide:
  - toc
---

<style>
.get-started-text {
  text-align: center;
  font-size: 2rem;
  font-weight: 700;
  background: linear-gradient(90deg, #007bff, #00bcd4);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* sub title */
.subtitle {
  text-align: center;
  font-size: 1.2rem;
  color: #666;
}
</style>

<div class="get-started-text">Volcengine Agent Development Kit</div>

<div class="subtitle">火山引擎智能体开发套件</div>

---

火山引擎智能体框架 **VeADK（Volcengine Agent Development Kit）**，是由**火山引擎**推出的为 Agent 智能体的应用构建提供开发、部署、观测、评测等全流程云原生解决方案。相较于现有的智能体开发框架，VeADK 具备与火山引擎产品体系深度融合的优势，帮助开发者更高效地构建企业级 AI 智能体应用。

!!! tip "快速开始"
    通过以下方式安装 VeADK：
    === "稳定版"

        ```bash
        pip install veadk-python
        ```

    === "抢先版"

        ```bash
        pip install git+https://github.com/volcengine/veadk-python.git@main
        ```

    ---

    或者您可以使用 VeADK 提供的镜像仓库：
    === "稳定版"

        ```
        veadk-cn-beijing.cr.volces.com/veadk/veadk-python:latest
        ```

    === "主分支预览版"

        ```
        veadk-cn-beijing.cr.volces.com/veadk/veadk-python:preview
        ```

    === "指定版本号"

        ```
        veadk-cn-beijing.cr.volces.com/veadk/veadk-python:0.2.20
        ```

<div class="grid" markdown>

[快速开始 :fontawesome-solid-paper-plane:](quickstart.md){ .openai-button }

[交互式教程 :fontawesome-solid-paper-plane:](quickstart.md){ .openai-button }

</div>

---

<div class="grid cards" markdown>

-   :material-account-group:{ .lg .middle } __多生态与模型兼容__

    ---

    VeADK 与 Google ADK 实现完全兼容，支持现有项目无缝迁移，可保障 API 接口的一致性与开发流程的连贯性。该套件不绑定特定 AI 模型，已适配 Doubao、DeepSeek 等多款主流大模型，具备灵活的模型接入能力。同时，其支持本地、云端、边缘等多类部署环境，并可兼容适配多种主流开发框架，具备极强的环境适配性与生态兼容性。

    [:octicons-arrow-right-24: Learn more](#)

-   :material-cloud-upload:{ .lg .middle } __云原生架构与快速部署__

    ---

    采用云原生架构设计，提供代码打包、镜像构建等多元化部署形式。通过整合火山引擎 VeFaaS、API 网关等核心服务，实现全开发流程的简化与高效流转。依托云部署项目模板，支持基于 CloudEngine 的一键式部署与发布，大幅提升上线效率。

    [:octicons-arrow-right-24: Learn more](#)

-   :material-eye:{ .lg .middle } __可观测性与评估能力__

    ---

    集成 CozeLoop、APMPlus、TLS 等多款工具组件，全面覆盖调用链路观测、日志存储检索及在线评测等核心需求。具备 Tracing 追踪能力，可精准记录智能体（Agent）执行过程中的关键路径与中间状态。构建智能体运行、评测、调优的一站式闭环支撑体系，为智能体的能力迭代与智能化升级提供坚实保障。

    [:octicons-arrow-right-24: Learn more](#)

-   :material-toolbox:{ .lg .middle } __内置丰富工具和生态集成__

    ---

    内置 Web Search、信息整合（VeSearch）、定制化内容查询（Web Scraper）等多款实用工具，满足基础业务场景需求。支持通过自定义MCP工具扩展功能边界，可实现飞书Lark、AI数据湖（LAS）等第三方服务及火山引擎生态服务的无缝对接。云端沙箱工具处于规划阶段（即将正式上线），涵盖 Computer sandbox、Browser sandbox、Code sandbox 等核心类型，将进一步拓展工具应用场景。支持通过函数定义方式快速创建自定义工具，使智能体可调用本地业务逻辑代码，精准完成特定业务任务。

    [:octicons-arrow-right-24: Learn more](#)

-   :material-database:{ .lg .middle } __完善的记忆与知识库支持__

    ---

    提供短期记忆与长期记忆的完整解决方案：短期记忆可基于 Viking 记忆库、MySQL 云数据库实现存储；长期记忆则依托 Viking DB、云搜索服务构建。支持记忆数据的向量化存储、高效检索、智能优化及自动摘要，确保智能体具备上下文感知能力与知识沉淀能力。VeADK 以 Llama-index 作为知识库核心处理入口，开发者可上传文本、文件及目录等多类型数据，系统将自动完成数据切片处理，降低知识库构建门槛。

    [:octicons-arrow-right-24: Learn more](#)

-   :material-shield-lock:{ .lg .middle } __企业级安全防护__

    ---

    依托火山引擎 Agent Identity 构建一站式身份鉴权体系，并结合权限管理平台提供全流程服务支撑。在身份管理层面，支持用户池管理、企业 IdP（SAML/OIDC）集成及第三方身份联合认证；在工作负载身份管理层面，可为智能体/工具分配唯一数字身份，并维护属性标签实现精准标识。提供第三方凭据托管功能，通过加密方式托管 API Key 与 OAuth 令牌，从根源杜绝明文凭据泄露风险。在权限管控方面，采用基于属性与上下文的动态授权机制，实现细粒度权限控制，保障服务访问安全。

    [:octicons-arrow-right-24: Learn more](#)
</div>

- **生态兼容**：与 Google ADK 完全兼容。
- **快速部署**：本地项目分钟级部署云端，提供代码打包、镜像构建等多种部署形式，简化上线流程。
- **一证通行**：基于火山引擎AK/SK进行企业级统一身份和密钥管理，确保安全访问和权限控制。

## VeADK Famliy

VeADK 各组件与火山引擎相关产品的结合矩阵：

| **组件** | **火山引擎产品** | **说明** |
| :-- | :-- | :-- |
| **大模型** | [**火山方舟**](https://www.volcengine.com/product/ark) | 一站式大模型开发平台，提供各类语言模型、多模态模型的推理服务 |
| **提示词工程** | [**PromptPilot**](https://promptpilot.volcengine.com/) | 提供提示词管理、优化能力 |
| **工具** | [**火山方舟大模型生态广场**](https://www.volcengine.com/mcp-marketplace) | 提供各类 MCP Server，丰富工具一键直连 |
|  | [**Web search**](https://www.volcengine.com/docs/85508/1650263)（融合信息搜索API）| 融合信息搜索，提供公域数据搜索功能 |
|  | [**VeSearch**](https://www.volcengine.com/docs/85508/1512748)（联网问答Agent） | 提供信息搜索与云端自动整合功能 |
|  | [**Web Scraper**](https://www.volcengine.com/docs/84296/1545470) | 定制化内容查询（邀测） |
|  | [**飞书 Lark**](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/mcp_integration/mcp_introduction) | 进行飞书相关操作 |
|  | [**AI 数据湖服务 LAS(Lake AI Service)**](https://www.volcengine.com/product/las)| 提供开放、低成本、高性能的AI数据湖，海量数据存储与查询能力 |
| **短期记忆** | [**mysql**](https://www.volcengine.com/docs/6313) | 提供使用 MySQL 数据库存储短期记忆，提供高性能读写能力，可实现持久化 |
|  | [**PostgreSQL**](https://www.volcengine.com/product/rds-pg) | 提供使用 PostgreSQL 数据库存储短期记忆，提供高性能读写能力，可实现持久化 |
|  | [**火山引擎云数据库 MySQL 版**](https://www.volcengine.com/product/rds-mysql) | 记忆存储 |
| **长期记忆** | [**云搜索服务**](https://www.volcengine.com/product/es)(OpenSearch) | 兼容Elasticsearch、OpenSearch等，支持全文搜索、向量搜索、混合搜索、AI搜索、时空检索等 |
|  | [**redis**](https://www.volcengine.com/product/redis) | Redis 作为长期记忆存储，支持 Redisearch 功能 |
|  | [**viking**](https://www.volcengine.com/docs/84313/1254437) | 知识向量化存储和检索 |
| **知识库**（链接数据源） | [**viking**](https://www.volcengine.com/docs/84313/1254437) | 知识向量化存储和检索 |
|  | [**mysql**](https://www.volcengine.com/docs/6313) | 提供使用 MySQL 数据库存储短期记忆，提供高性能读写能力，不具备向量搜索功能 |
|  | [**redis**](https://www.volcengine.com/product/redis) | Redis 作为长期记忆存储，支持 Redisearch |
|  | [**云搜索服务**](https://www.volcengine.com/product/es)(OpenSearch) | 知识向量化存储和检索 |
| **可观测** | [**应用性能监控全链路版**](https://www.volcengine.com/product/apmplus)(APMPlus) | 调用链路观测 |
|  | [**扣子罗盘**](https://www.coze.cn/loop)(CozeLoop) | 调用链路观测 |
|  | [**日志服务**](https://www.volcengine.com/product/tls)(TLS) | 调用链路观测、日志存储与检索 |
| **评测** | [**扣子罗盘**](https://www.coze.cn/loop)(CozeLoop) | 在线评测 |
| **云部署** | [**火山引擎函数服务**](https://www.volcengine.com/product/vefaas)(VeFaaS) | 提供一键上云能力 |
|  | [**火山引擎 API 网关**](https://www.volcengine.com/product/apig) | 提供鉴权、路由等能力 |
|  | [**火山引擎持续交付**](https://www.volcengine.com/product/cp) | 提供用户仓库向 VeFaaS 进行基于镜像的持续交付部署 |
|  | [**火山引擎镜像仓库**](https://www.volcengine.com/product/cr) | 提供用户代码镜像托管维护 |
