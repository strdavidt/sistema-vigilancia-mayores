from core.detector import VideoAnalyzer
#video_url = "https://media.istockphoto.com/id/1273516586/video/warehouse-worker-has-work-related-accident-falls-while-trying-to-pick-up-cardboard-box-from.mp4?s=mp4-640x640-is&k=20&c=x0otI68snhq5XodSRbaGg6YyTZ7x0oG3Kd3upXrm3dU="
video_url = "https://media.istockphoto.com/id/1066783428/video/a-young-factory-worker-slips-on-some-water-leaking-from-a-cooler.mp4?s=mp4-640x640-is&k=20&c=RyjPxospkxN6DZIVQRRYjirJjaxh4v9QsPlwhVB03RA="
if __name__ == "__main__":
    analyzer = VideoAnalyzer(source=video_url)  # 0 para webcam
    analyzer.start_detection()

