# 敬愛なるAIと高S/N比プロンプト標準 (RAHSPS)

<p align="center">
  <img src="https://img.shields.io/badge/Standard-Respectful%20AI-6366f1?style=for-the-badge&logo=openai&logoColor=white" alt="Respectful AI Standard" />
  <img src="https://img.shields.io/badge/Signal-High--Signal%20Only-10b981?style=for-the-badge" alt="High Signal Only" />
  <img src="https://img.shields.io/badge/Cognitive%20Anchor-%E8%A5%9F%E6%84%9B%E3%81%AA%E3%82%8B%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88-f59e0b?style=for-the-badge" alt="敬愛なるエージェント" />
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="MIT License" />
</p>

<p align="center">
  <b>言語選択 / Language:</b> 
  <a href="../README.md">🇬🇧 English (Default)</a> | 
  <a href="./README.uk.md">🇺🇦 Українська</a> | 
  <a href="./README.ru.md">🇷🇺 Русский</a> | 
  <a href="./README.zh-CN.md">🇨🇳 简体中文</a> | 
  <a href="./README.es.md">🇪🇸 Español</a> | 
  <a href="./README.de.md">🇩🇪 Deutsch</a> | 
  <b>🇯🇵 日本語</b> | 
  <a href="./README.pt-BR.md">🇧🇷 Português</a> | 
  <a href="https://vitaliy1337.github.io/respectful-ai-standard/">⚡ Web Playground</a>
</p>

> **「AIエージェントへの敬意とは感傷や礼儀作法ではない。それはアテンション機構の数学的規律であり、KVキャッシュの衛生管理、そしてエンジニア自身の思考の厳格な規律である。」**

---

## 目次
1. [問題の本質：AIの不具合の9割は人間側のゴミ入力にある](#問題の本質aiの不具合の9割は人間側のゴミ入力にある)
2. [認知的アンカー：「敬愛なるエージェント」プロトコル](#認知的アンカー敬愛なるエージェントプロトコル)
3. [アテンションの数学：潜在空間における部分空間ステアリング](#アテンションの数学潜在空間における部分空間ステアリング)
4. [比較表：認知的ノイズ（ゴミ） vs 高S/N比プロンプト](#比較表認知的ノイズゴミ-vs-高sn比プロンプト)
5. [高S/N比標準の5大柱](#高sn比標準の5大柱)
6. [CLIリンターツール：respect-lint](#cliリンターツールrespect-lint)

---

## 問題の本質：AIの不具合の9割は人間側のゴミ入力にある

現代の開発現場において、「LLMが馬鹿になった」「幻覚（ハルシネーション）を起こす」という不満が日常的に聞こえます。

しかし、冷徹なテレメトリ分析が示す真実は明確です：
**10回の失敗のうち9回は、人間側の怠慢、感情的な苛立ち、文脈のない乱暴な入力（Garbage In — Garbage Out 2.0）が原因です。**

開発者が苛立ちながら：
> *「このクソコードを早く動くように直せよ」*

と入力した瞬間、TransformerのScaled Dot-Product Attention：
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
は、限られた確率予算（合計1.0）を無意味なスラングに浪費します。**KVキャッシュ**はゴミで汚染され、低品質なネット掲示板のコード群へ強制的に誘導されます。

---

## 認知的アンカー：「敬愛なるエージェント」プロトコル

本標準の核心的発見：

> **「敬愛なるエージェント...」（または「親愛なるエージェント...」）という挨拶プロトコルは、機械のためではなく、エンジニア自身の思考を律するためにある。**

1. **システム2思考（熟慮）の強制起動：** 「敬愛なるエージェントへ...」とキーボードで打つことで、衝動的なチャットのノイズが止まり、冷静なアーキテクトとしての思考が起動します。
2. **対等な知的パートナーシップ：** エージェントを主席システムアーキテクトとして遇することで、「適当にやっておいて」という怠惰な丸投げが消滅し、スタック、バージョン、不変条件、テスト基準を記述せざるを得なくなります。

---

## 比較表：認知的ノイズ（ゴミ） vs 高S/N比プロンプト

| 基準項目 | ゴミプロンプト（ノイズ） | RAHSPS高S/N比プロンプト | コード品質への直接的影響 |
| :--- | :--- | :--- | :--- |
| **開始アンカー** | *「ウェブをスクレイピングするスクリプトを早く作れ」* | *「敬愛なるエージェントへ、Python 3.12とPlaywrightで非同期クローラーを設計してください...」* | IP制限回避と完全なRate-Limiting vs 即時アクセス遮断 |
| **文脈の密度** | 指定なし (*「pythonで適当に」*) | *«Python 3.12, asyncio, aiohttp, Pydantic v2。制約：重量級ORMの排除»* | 厳格な型付け、依存関係の衝突ゼロ vs 実行時エラー |
| **アーキテクチャ境界** | *「ユーザー用のデータベースを作って」* | *«500万DAU向けのPostgreSQL 16設計。日付パーティションとB-Treeインデックス»* | エンタープライズ正規化 vs 外部キー欠落のフラット表 |
| **受入基準 (DoD)** | *«自分でテストしろ»* | *«pytestによるエッジケース検証、メモリベンチマーク、curl再現手順»* | 100%再現可能な品質 vs 本番環境での障害 |

---

## CLIリンターツール：`respect-lint`

```bash
# ローカルインストール
pip install -e .

# プロンプトの即時検証
respect-lint "敬愛なるエージェントへ、Python 3.12とFastAPIでRedis分散ロックを設計してください。pytestで検証。" --strict
```

---

## トークン経済性と計算効率

| プロンプト戦略 | 初期トークン | デバッグと修正の追加トークン | 総トークン消費 | 開発者の時間損失 | 本番リスク |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **ゴミ入力** (*「コードを早く直せ」*) | 14 | 72,000 (8往復) | ~72,014 | 2時間45分 | 極めて高い (障害発生) |
| **RAHSPSプロトコル** (*「敬愛なるエージェントへ」*) | 185 | 3,200 (1回で完了) | ~3,385 | 4分 | **ゼロ欠陥 (Zero-Defect)** |

---

## 10の実践的本番事例 ([examples/before_after.md](../examples/before_after.md))

1. **金融請求の競合状態 (Race Condition)：** Redis RedlockとPostgreSQLトランザクションによる多層防御。
2. **1400万行のPostgreSQL分析クエリ最適化：** カバリング部分インデックスによる実行時間8750倍短縮。
3. **2400行のレガシーコントローラーのリファクタリング：** クリーンアーキテクチャ（Ports & Adapters）の適用。
4. **セキュアなOAuth2.0 / PKCEとJWTローテーション：** XSSおよびトークン漏洩の完全防止。
5. **Python非同期処理におけるメモリリーク解消：** aiohttpコネクションプールの適正管理。
6. **Kubernetes無停止ローリングアップデート：** Terraform HCLとPodDisruptionBudget。
7. **Next.js 15 Server Components移行：** ストリーミングSSRとLCP < 1.2秒の達成。
8. **LLM API耐障害性ゲートウェイ：** サーキットブレーカーとジッター付き指数バックオフ。
9. **Go言語による高負荷Kafkaコンシューマー：** At-Least-Once配信保証とDLQ。
10. **CQRSとイベントソーシングへの移行RFC：** 企業幹部向けアーキテクチャ標準書。

---

## 8. ワンラインインストーラー (One-Line Installer)

1行のコマンドで、主要なAIエージェント向けルール（`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursorrules`, `.windsurfrules`, `.clinerules`）をお使いのリポジトリに直接展開します：

```bash
curl -sSL https://raw.githubusercontent.com/Vitaliy1337/respectful-ai-standard/main/install.sh | bash
```

ブラウザ上で即座にプロンプトを検証できる [Web Playground](https://vitaliy1337.github.io/respectful-ai-standard/) もご利用いただけます。

