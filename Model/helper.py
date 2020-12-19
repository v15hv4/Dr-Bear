from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler
from keras.preprocessing.sequence import pad_sequences
import torch

output_dir = './model_save'


MAX_LEN = 64

# # Tell PyTorch to use the GPU over CPU.
# if torch.cuda.is_available():
#     device = torch.device("cuda")
#     print('There are %d GPU(s) available.' % torch.cuda.device_count())
#     print('We will use the GPU:', torch.cuda.get_device_name(0))
# else:
#     print('No GPU available, using the CPU instead.')
#     device = torch.device("cpu")

# in case there is some assert error by pytorch,
# use the below instead of the above.
# basically sets the hardware to be used as CPU
device = torch.device("cpu")

# Load a trained model and vocabulary that you have fine-tuned
model = DistilBertForSequenceClassification.from_pretrained(output_dir)
tokenizer = DistilBertTokenizer.from_pretrained(output_dir)

# Copy the model to the GPU.
model.to(device)

soft = torch.nn.Softmax()


def fun(sentences):
    """
    takes in sentences
    returns predicted labels
    """
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
            sent,                      # Sentence to encode.
            add_special_tokens=True,  # Add '[CLS]' and '[SEP]'
        )

        input_ids.append(encoded_sent)

    # Pad our input tokens
    input_ids = pad_sequences(input_ids, maxlen=MAX_LEN,
                              dtype="long", truncating="post", padding="post")
    # print(input_ids)
    # print(torch.tensor(input_ids))
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
        prediction_data, sampler=prediction_sampler, batch_size=batch_size)

    ################################# PREDICTING ##############################

    # Put model in evaluation mode
    model.eval()

    # Tracking variables
    predictions = []

    # Predict
    for batch in prediction_dataloader:
        # Add batch to GPU
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
        # predictions.append(logits)
        # print(logits)
        for logit in logits:
            print(logit)
            final_predictions.append(logit)
        # predictions.append()

        print('DONE.')

    return final_predictions


print(fun(['market is very good', 'what a shit time to be in!',
           'The international electronic industry company Elcoteq has laid off tens of employees from its Tallinn facility ; contrary to earlier layoffs the company contracted the ranks of its office workers , the daily Postimees reported .']))
