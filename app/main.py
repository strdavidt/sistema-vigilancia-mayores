from core.detector import VideoAnalyzer
video_url = "https://media.istockphoto.com/id/1066783428/video/a-young-factory-worker-slips-on-some-water-leaking-from-a-cooler.mp4?s=mp4-640x640-is&k=20&c=RyjPxospkxN6DZIVQRRYjirJjaxh4v9QsPlwhVB03RA="
if __name__ == "__main__":
    analyzer = VideoAnalyzer(source=video_url)  # 0 para webcam
    analyzer.start_detection()

