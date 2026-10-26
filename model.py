"""PyTorch port of the CNN-LSTM architecture in the archived Aruna notebook.

The later pure-LSTM overwrite in that notebook is deliberately not used.
Causal convolution, pool strides, hidden sizes and flatten order are preserved.
Weights are newly trained; TensorFlow checkpoints are not converted.
"""

from torch import nn
from torch.nn import functional as F


class CNNLSTM(nn.Module):
    def __init__(self, window=30):
        super().__init__()
        self.conv1 = nn.Conv1d(3, 64, 5)
        self.conv2 = nn.Conv1d(64, 32, 3)
        self.pool = nn.MaxPool1d(2, stride=1)
        self.lstm = nn.LSTM(32, 128, batch_first=True)
        self.head = nn.Sequential(
            nn.Linear((window - 2) * 128, 64),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(64, 16),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(16, 1),
        )

    def forward(self, x):
        x = x.transpose(1, 2)
        x = self.pool(F.relu(self.conv1(F.pad(x, (4, 0)))))
        x = self.pool(F.relu(self.conv2(F.pad(x, (2, 0)))))
        x, _ = self.lstm(x.transpose(1, 2))
        return self.head(x.reshape(len(x), -1))
