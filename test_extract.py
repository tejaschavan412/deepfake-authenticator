from app.video.extractor import FrameExtractor
from app.core.logger import setup_logger

logger = setup_logger(__name__)
frames = FrameExtractor.extract(
    "uploads/videos/smaplevideo.mp4",
    max_frames=5
)

logger.info(f"Extracted {len(frames)} frames")

for frame in frames[:5]:
    logger.info(frame)