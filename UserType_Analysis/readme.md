# readme

## 目标：

分析doc用户和drive用的重叠度。

需要从以下角度考虑：

- doc用户和drive用户在两周内使用的频率？
- 行业间使用doc和drive的频率有无特点？
- 用户层面，doc用户活跃和drive用户活跃之间的在统计上有无关联？
- 能否使用图表清晰的表达两个产品活跃度之间的关系？
- 在公司层级、行业层级，两个产品的活跃度又如何？


## 数据结构说明：

vid_: 用户id
corpid_: 公司id
_c2: 两周内打开次数
ds: 从该日期开始的两周内的截面数据
corpid: 公司id
corp_memeber: 公司人数规模
wakeup_member: 两周内唤醒该软件的人数
industryid: 行业id
ispay: 该公司是否为drive付费用户
capacity: 该公司drive容量
used_capacity: 忽略
used_capacity2: 该公司已使用的drive容量