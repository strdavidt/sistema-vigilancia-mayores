from core.detector import VideoAnalyzer

# Puedes cambiar esta URL por otra o usar 0 para webcam en tiempo real
# persona se cae 
video_url = "https://media.istockphoto.com/id/1066783428/video/a-young-factory-worker-slips-on-some-water-leaking-from-a-cooler.mp4?s=mp4-640x640-is&k=20&c=RyjPxospkxN6DZIVQRRYjirJjaxh4v9QsPlwhVB03RA="
#persona sale de la vista
#video_url = "https://media.istockphoto.com/id/1081146836/video/leaving-home-with-bike.mp4?s=mp4-640x640-is&k=20&c=6kh7cHYPMt9NZCo7BIq0HdQOXMeJgZy1S5nW3axlq24="
if __name__ == "__main__":
    analyzer = VideoAnalyzer(source=video_url)
    analyzer.start_detection()
