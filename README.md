# novelai-embedded-prompt
👋 **Say Goodbye to LOOOONG File Name!**

NovelAIで生成されたイラストのプロンプトとシードを画像にメタデータとして埋め込むアプリです。  
プロンプトを埋め込んだあとは自動で連番となるように画像をリネームして保存します。

現在PNG形式の画像のみ対応しています。

## Dependencies
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI) (for GUI)

## Usage
### GUI (Recommended)
1. ```start-gui.bat```をクリックする。
1. 処理をしたい画像が含まれるディレクトリを選択する。
1. ファイル名にプレフィックスを付けたい場合は、プレフィックスを設定する。
1. ```Run```を押す。

### CUI
1. ```start.bat```をクリックする。
1. 処理をしたい画像が含まれるディレクトリのパスを入力する。
1. ファイル名にプレフィックスを付けたい場合は、プレフィックスを入力する。