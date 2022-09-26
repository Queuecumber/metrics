r"""Root package info."""
import logging as __logging
import os

from torchmetrics.__about__ import *  # noqa: F401, F403

_logger = __logging.getLogger("torchmetrics")
_logger.addHandler(__logging.StreamHandler())
_logger.setLevel(__logging.INFO)

_PACKAGE_ROOT = os.path.dirname(__file__)
_PROJECT_ROOT = os.path.dirname(_PACKAGE_ROOT)

from torchmetrics import functional  # noqa: E402
from torchmetrics.aggregation import CatMetric, MaxMetric, MeanMetric, MinMetric, SumMetric  # noqa: E402
from torchmetrics.audio import (  # noqa: E402
    PermutationInvariantTraining,
    ScaleInvariantSignalDistortionRatio,
    ScaleInvariantSignalNoiseRatio,
    SignalDistortionRatio,
    SignalNoiseRatio,
)
from torchmetrics.classification import (  # noqa: E402
    AUC,
    AUROC,
    ROC,
    Accuracy,
    AveragePrecision,
    BinnedAveragePrecision,
    BinnedPrecisionRecallCurve,
    BinnedRecallAtFixedPrecision,
    CalibrationError,
    CohenKappa,
    ConfusionMatrix,
    CoverageError,
    Dice,
    F1Score,
    FBetaScore,
    HammingDistance,
    HingeLoss,
    JaccardIndex,
    LabelRankingAveragePrecision,
    LabelRankingLoss,
    MatthewsCorrCoef,
    Precision,
    PrecisionRecallCurve,
    Recall,
    Specificity,
    StatScores,
)
from torchmetrics.collections import MetricCollection  # noqa: E402
from torchmetrics.image import (  # noqa: E402
    ErrorRelativeGlobalDimensionlessSynthesis,
    MultiScaleStructuralSimilarityIndexMeasure,
    PeakSignalNoiseRatio,
    SpectralAngleMapper,
    SpectralDistortionIndex,
    StructuralSimilarityIndexMeasure,
    UniversalImageQualityIndex,
)
from torchmetrics.metric import Metric  # noqa: E402
from torchmetrics.regression import (  # noqa: E402
    ConcordanceCorrCoef,
    CosineSimilarity,
    ExplainedVariance,
    KLDivergence,
    MeanAbsoluteError,
    MeanAbsolutePercentageError,
    MeanSquaredError,
    MeanSquaredLogError,
    PearsonCorrCoef,
    R2Score,
    SpearmanCorrCoef,
    SymmetricMeanAbsolutePercentageError,
    TweedieDevianceScore,
    WeightedMeanAbsolutePercentageError,
)
from torchmetrics.retrieval import (  # noqa: E402
    RetrievalFallOut,
    RetrievalHitRate,
    RetrievalMAP,
    RetrievalMRR,
    RetrievalNormalizedDCG,
    RetrievalPrecision,
    RetrievalPrecisionRecallCurve,
    RetrievalRecall,
    RetrievalRecallAtFixedPrecision,
    RetrievalRPrecision,
)
from torchmetrics.text import (  # noqa: E402
    BLEUScore,
    CharErrorRate,
    CHRFScore,
    ExtendedEditDistance,
    MatchErrorRate,
    Perplexity,
    SacreBLEUScore,
    SQuAD,
    TranslationEditRate,
    WordErrorRate,
    WordInfoLost,
    WordInfoPreserved,
)
from torchmetrics.wrappers import (  # noqa: E402
    BootStrapper,
    ClasswiseWrapper,
    MetricTracker,
    MinMaxMetric,
    MultioutputWrapper,
)

__all__ = [
    "functional",
    "Accuracy",
    "AUC",
    "AUROC",
    "AveragePrecision",
    "BinnedAveragePrecision",
    "BinnedPrecisionRecallCurve",
    "BinnedRecallAtFixedPrecision",
    "BLEUScore",
    "BootStrapper",
    "CalibrationError",
    "CatMetric",
    "ClasswiseWrapper",
    "CharErrorRate",
    "CHRFScore",
    "ConcordanceCorrCoef",
    "CohenKappa",
    "ConfusionMatrix",
    "CosineSimilarity",
    "CoverageError",
    "Dice",
    "TweedieDevianceScore",
    "ErrorRelativeGlobalDimensionlessSynthesis",
    "ExplainedVariance",
    "ExtendedEditDistance",
    "F1Score",
    "FBetaScore",
    "HammingDistance",
    "HingeLoss",
    "JaccardIndex",
    "KLDivergence",
    "LabelRankingAveragePrecision",
    "LabelRankingLoss",
    "MatchErrorRate",
    "MatthewsCorrCoef",
    "MaxMetric",
    "MeanAbsoluteError",
    "MeanAbsolutePercentageError",
    "MeanMetric",
    "MeanSquaredError",
    "MeanSquaredLogError",
    "Metric",
    "MetricCollection",
    "MetricTracker",
    "MinMaxMetric",
    "MinMetric",
    "MultioutputWrapper",
    "MultiScaleStructuralSimilarityIndexMeasure",
    "PearsonCorrCoef",
    "PermutationInvariantTraining",
    "Perplexity",
    "Precision",
    "PrecisionRecallCurve",
    "PeakSignalNoiseRatio",
    "R2Score",
    "Recall",
    "RetrievalFallOut",
    "RetrievalHitRate",
    "RetrievalMAP",
    "RetrievalMRR",
    "RetrievalNormalizedDCG",
    "RetrievalPrecision",
    "RetrievalRecall",
    "RetrievalRPrecision",
    "RetrievalPrecisionRecallCurve",
    "RetrievalRecallAtFixedPrecision",
    "ROC",
    "SacreBLEUScore",
    "SignalDistortionRatio",
    "ScaleInvariantSignalDistortionRatio",
    "ScaleInvariantSignalNoiseRatio",
    "SignalNoiseRatio",
    "SpearmanCorrCoef",
    "Specificity",
    "SpectralAngleMapper",
    "SpectralDistortionIndex",
    "SQuAD",
    "StructuralSimilarityIndexMeasure",
    "StatScores",
    "SumMetric",
    "SymmetricMeanAbsolutePercentageError",
    "TranslationEditRate",
    "UniversalImageQualityIndex",
    "WeightedMeanAbsolutePercentageError",
    "WordErrorRate",
    "WordInfoLost",
    "WordInfoPreserved",
]
