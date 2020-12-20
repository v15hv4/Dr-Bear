# All the necessary imports
# math
import numpy as np

# Data preporcessing
from keras.preprocessing.sequence import pad_sequences

# Models, Tokenizers
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

# Dataset handling
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler

# handling model output
import torch


# the place where we have our DistilBERT model
output_dir = "./model_save"

# maximum length of the comment/tweet; median lies below 64.
MAX_LEN = 64

# telling pytorch to use CPU for predicting outputs
device = torch.device("cpu")

# Load a trained model and vocabulary that you have fine-tuned
model = DistilBertForSequenceClassification.from_pretrained(output_dir)
tokenizer = DistilBertTokenizer.from_pretrained(output_dir)

# Copy the model to the GPU.
model.to(device)

# softmax layer for converting predicted logits into probability
soft = torch.nn.Softmax()


def predict_sentiment(sentences):
    """
    takes in a list of sentences
    returns a list of corresponding integer values from (-1, 0, +1)
    """
    # list storing final predictions
    final_predictions = []

    # Tokenize all of the sentences and map the tokens to thier word IDs.
    input_ids = []

    # For every sentence...
    for sent in sentences:
        # `encode` will:
        #   (1) Tokenize the sentence.
        #   (2) Prepend the `[CLS]` token to the start.
        #   (3) Append the `[SEP]` token to the end.
        #   (4) Map tokens to their IDs.
        encoded_sent = tokenizer.encode(
            sent,  # Sentence to encode.
            add_special_tokens=True,  # Add '[CLS]' and '[SEP]'
        )

        input_ids.append(encoded_sent)

    # Pad our input tokens
    input_ids = pad_sequences(
        input_ids, maxlen=MAX_LEN, dtype="long", truncating="post", padding="post"
    )

    # Create attention masks
    attention_masks = []

    # Create a mask of 1s for each token followed by 0s for padding
    for seq in input_ids:
        seq_mask = [float(i > 0) for i in seq]
        attention_masks.append(seq_mask)

    ################################# DATA LOADING ##############################

    # Convert to tensors.
    prediction_inputs = torch.tensor(input_ids)
    prediction_masks = torch.tensor(attention_masks)
    # prediction_labels = torch.tensor(labels)

    # Set the batch size.
    batch_size = 2

    # Create the DataLoader.
    # prediction_data = TensorDataset(prediction_inputs, prediction_masks, prediction_labels)
    prediction_data = TensorDataset(prediction_inputs, prediction_masks)
    prediction_sampler = SequentialSampler(prediction_data)
    prediction_dataloader = DataLoader(
        prediction_data, sampler=prediction_sampler, batch_size=batch_size
    )

    ################################# PREDICTING ##############################

    # Put model in evaluation mode
    model.eval()

    # Tracking variables
    # predictions = []

    # Predict
    for batch in prediction_dataloader:
        # use CPU
        batch = tuple(t.to(device) for t in batch)

        # Unpack the inputs from our dataloader
        b_input_ids, b_input_mask = batch

        # Telling the model not to compute or store gradients, saving memory and
        # speeding up prediction
        with torch.no_grad():
            # Forward pass, calculate logit predictions
            outputs = model(b_input_ids, attention_mask=b_input_mask)

        logits = outputs[0]

        # Move logits and labels to CPU
        logits = logits.detach().cpu().numpy()

        # Store predictions and true labels
        for logit in logits:
            final_predictions.append(
                np.argmax(
                    soft(torch.FloatTensor(logit)).tolist()
                )-1
            )

    return final_predictions
