# Báo cáo lab: chọn tracker cho 5 video

**Nhóm:** BOMBE **Thành viên:** Vũ Quốc Huy (2A202602929), Nguyễn Hữu Thành (2A202602813)

Detector cố định: `yolo26n.pt`, ảnh 640 px, Re-ID `osnet_x0_25_msmt17`. Không đổi các mục này trong bài nộp chính.

## 1. Cấu hình đã chọn

Mỗi video: tracker bạn nộp, `conf`, `iou`, điều bạn **nhìn thấy** trên video, và một cấu hình đã thử rồi loại.

| Video | Tracker | conf | iou | Quan sát khi xem video | Đã thử nhưng loại |
|---|---|---|---|---|---|
| video_1 (quảng trường, tĩnh, ban ngày) | StrongSORT | 0.15 | 0.5 | Người rõ ở tiền cảnh có hộp; người nhỏ hoặc chồng lấn trong đám đông có thể bị thiếu hộp hoặc hộp giao nhau. | StrongSORT 0.3/0.5: trên 150 frame, HOTA và IDF1 thấp hơn 0.15/0.5, dù MOTA cao hơn. |
| video_2 (phố đêm, tĩnh, rất đông) | ByteTrack | 0.3 | 0.5 | Góc nhìn trên cao, nhiều người; người rõ có hộp, người nhỏ hoặc khuất giữa đám đông khó theo dõi. | ByteTrack 0.5/0.5: 1.122 detection/150 frame so với 1.313 ở 0.3/0.5. StrongSORT 0.3/0.5 chậm hơn, chưa thấy cải thiện rõ ở khung đối chiếu. |
| video_3 (camera di động, ảnh nhỏ) | ByteTrack | 0.3 | 0.5 | Người ở tiền cảnh bị cắt sát mép khung hình; người phía xa rất nhỏ và khó phát hiện. | ByteTrack 0.5/0.5: 553 detection/150 frame so với 593 ở 0.3/0.5. StrongSORT 0.3/0.5 chậm hơn, chưa thấy cải thiện rõ ở khung đối chiếu. |
| video_4 (trong nhà, camera di chuyển) | ByteTrack | 0.3 | 0.5 | Hộp bám được người trong trung tâm thương mại; camera di chuyển và kính phản chiếu làm cảnh phức tạp. | ByteTrack 0.5/0.5: 773 detection/150 frame so với 809 ở 0.3/0.5. StrongSORT 0.3/0.5 chậm hơn, chưa thấy cải thiện rõ ở khung đối chiếu. |
| video_5 (trên xe bus, giao lộ đông) | ByteTrack | 0.3 | 0.5 | Camera rung; người đi bộ nhỏ ở hai bên đường, cùng nhiều xe và vật thể nền. | ByteTrack 0.5/0.5: 518 detection/150 frame so với 673 ở 0.3/0.5; có thể bỏ người nhỏ. StrongSORT 0.3/0.5 chậm hơn, chưa thấy cải thiện rõ ở khung đối chiếu. |

## 2. Số liệu video_1

Dán bảng HOTA / MOTA / IDF1 do `scripts/evaluate_practice.py` in ra.

```
HOTA: 29.190
MOTA: 19.907
IDF1: 32.573
```

`video_2` đến `video_5` không có nhãn trong gói lab. Không điền số cho các video đó.

## 3. Phân tích

Với **ít nhất hai video** (nên gồm một video bạn chỉ đánh giá bằng mắt), viết 3–5 câu:

- Tracker đã chọn giữ ID tốt hơn, hay ít hộp giả hơn, ở điểm nào bạn nhìn thấy?
- Cảnh đó (đứng yên / chuyển động, đông / thưa, sáng / tối, trong nhà / ngoài trời) khiến tracker này hợp hơn tracker kia như thế nào?

Ở baseline ByteTrack trên 150 frame đầu `video_1`, ID 2 và ID 3 được giữ xuyên suốt đoạn thử; hộp của hai người tiền cảnh di chuyển ổn định theo người. Đây là một đoạn ID bám ổn để đối chiếu với các cấu hình khác.

Trong 150 frame đầu video_1, StrongSORT 0.3/0.5 đạt HOTA 31.890 và IDF1 29.853, cao hơn ByteTrack 0.3/0.5 (HOTA 31.147, IDF1 27.228). StrongSORT 0.15/0.5 tăng HOTA lên 35.386 và IDF1 lên 37.518, nhưng MOTA giảm còn 14.798 so với 16.485 ở 0.3/0.5. Preview cho thấy các người rõ ở tiền cảnh có hộp, còn người nhỏ hoặc chồng lấn dễ bị bỏ sót. Vì ưu tiên giữ ID theo HOTA/IDF1, mình chọn StrongSORT 0.15/0.5; kết quả chính thức đủ 600 frame là HOTA 29.190, MOTA 19.907, IDF1 32.573.

Ở video_4, ByteTrack và StrongSORT tạo hộp khá giống nhau trên khung hình đối chiếu trong trung tâm thương mại. StrongSORT xử lý 150 frame trong 70.1 giây, còn ByteTrack mất 33.8 giây; chưa thấy cải thiện rõ để bù thời gian tăng thêm. Với ByteTrack, conf 0.5 giảm số detection từ 809 xuống 773, còn conf 0.15 tăng lên 845, nên giữ 0.3 làm mức trung gian. IoU 0.4 và 0.7 cho số detection giống 0.5 trong lượt thử này.

## 4. Nếu có thêm thời gian

Một hoặc hai câu: bạn sẽ thử tiếp điều gì (Re-ID khác, quét `conf` mịn hơn, xem frame gây lỗi…).

Xem lại các đoạn người bị che khuất hoặc ở xa để so sánh ID theo thời gian, nhất là video_3 và video_5 có camera chuyển động. Nếu có nhãn cho bốn video còn lại, dùng chúng để xác nhận lựa chọn ByteTrack hay StrongSORT.
