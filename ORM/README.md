```plantuml
hide methods

class "カテゴリー" as category {
  カテゴリ名
}
class "タグ" as tag {
    タグ名
}

class "記事" as article {
    タイトル
    カテゴリ[外部]
    タグ[外部]
}

category "1" -- "1" article
article "1..*" - "0..*" tag
```