import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Dropout, LayerNormalization, MultiHeadAttention, Conv1D, GlobalMaxPooling1D, concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

# Definizione del modello Transformer
def transformer_model(input_shape):
    inputs = Input(shape=input_shape)

    # Strato di normalizzazione
    x = LayerNormalization(epsilon=1e-6)(inputs)

    # Strato di attenzione multi-head
    num_heads = 4
    x = MultiHeadAttention(num_heads=num_heads, key_dim=32)(x, x)
    x = Dropout(0.1)(x)
    x = LayerNormalization(epsilon=1e-6)(x)

    # Strato feed-forward
    x = Dense(64, activation='relu')(x)
    x = Dropout(0.1)(x)
    x = LayerNormalization(epsilon=1e-6)(x)

    transformer_output = x

    model = Model(inputs=inputs, outputs=transformer_output)
    return model

# Definizione della rete neurale esistente
def neural_network_model(input_shape):
    inputs = Input(shape=input_shape)

    # Strati convoluzionali
    x = Conv1D(64, kernel_size=3, activation='relu')(inputs)
    x = GlobalMaxPooling1D()(x)

    neural_output = x

    model = Model(inputs=inputs, outputs=neural_output)
    return model

# Dimensioni degli input
image_embedding_shape = (800, 1)
neural_network_input_shape = (800, 4)

# Creazione del modello Transformer
transformer = transformer_model(image_embedding_shape)

# Creazione della rete neurale esistente
neural_network = neural_network_model(neural_network_input_shape)

# Concatenazione dei due modelli
concatenated_output = concatenate([transformer.output, neural_network.output])

# Aggiunta di ulteriori strati se necessario
x = Dense(128, activation='relu')(concatenated_output)
x = Dropout(0.2)(x)
x = Dense(64, activation='relu')(x)
output = Dense(1, activation='sigmoid')(x)

# Creazione del modello finale
model = Model(inputs=[transformer.input, neural_network.input], outputs=output)

# Compilazione del modello
model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])

# Visualizzazione dell'architettura del modello
model.summary()
