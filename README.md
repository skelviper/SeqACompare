# SeqACompare

GUI基于tkinter库，序列比对基于Smith-Waterman Algorithm的一个快速进行序列比对软件。

## 打分表：

| 情况             | 变量名                  | 得分                      |
| ---------------- | ----------------------- | ------------------------- |
| 配对             | match_award             | 1                         |
| 不配对           | mismatch_penalty        | -2                        |
| 不确定的碱基     | N                       | -1                        |
| 产生空位         | gap_penalty             | -3                        |
| 空位延伸罚分修正 | Extendgap_recalibration | 1（在空位罚分-3的基础上） |

## 使用方法

+ 程序运行后，在Original Sequence上填写用fasta格式表示的原序列。
+ 在Sequencing Result上填写用fasta格式表示的正向反向两段测序结果，5‘->3'填在第一个。
+ 单击align，结果会在output窗口中输出。每次点击align会清空输出窗口。
+ clear按钮用于清空所有窗口内容。

## 待办事项

+ 输出时换行
+ 标尺