import java.io.IOException;
import java.util.Locale;
import javax.speech.*;
import javax.speech.recognition.*;
import javax.speech.synthesis.*;

public class PersonalAssistant {
    public static void main(String[] args) {
        try {
            // Criação do objeto Synthesizer para síntese de voz
            Synthesizer synthesizer = Central.createSynthesizer(null);
            synthesizer.allocate();
            synthesizer.resume();

            // Criação do objeto Recognizer para reconhecimento de fala
            Recognizer recognizer = Central.createRecognizer(null);
            recognizer.allocate();

            // Carregamento da gramática de comandos
            String grammarFile = "grammar.gram";
            recognizer.loadGrammar(new File(grammarFile));

            // Configuração do listener de eventos de reconhecimento
            recognizer.addResultListener(new ResultListener() {
                public void resultAccepted(ResultEvent e) {
                    try {
                        // Obtém a hipótese de reconhecimento
                        Result result = (Result) e.getSource();
                        String recognizedText = result.getBestFinalResultNoFiller();

                        // Processa o comando reconhecido
                        processCommand(recognizedText, synthesizer);
                    } catch (Exception ex) {
                        ex.printStackTrace();
                    }
                }
            });

            // Início do reconhecimento de fala contínuo
            recognizer.commitChanges();
            recognizer.requestFocus();
            recognizer.resume();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void processCommand(String command, Synthesizer synthesizer) throws IOException {
        if (command.contains("olá")) {
            synthesizer.speakPlainText("Olá, como posso ajudar?", null);
        } else if (command.contains("horas")) {
            String time = getCurrentTime();
            synthesizer.speakPlainText("Agora são " + time, null);
        } else if (command.contains("pesquisar")) {
            String query = command.replace("pesquisar", "").trim();
            String result = searchWikipedia(query);
            synthesizer.speakPlainText("Aqui está o que encontrei: " + result, null);
        } else if (command.contains("sair")) {
            synthesizer.speakPlainText("Até logo!", null);
            synthesizer.deallocate();
            System.exit(0);
        } else {
            synthesizer.speakPlainText("Desculpe, não entendi o comando.", null);
        }
    }

    public static String getCurrentTime() {
        // Obtenção da hora atual
        Calendar calendar = Calendar.getInstance();
        SimpleDateFormat timeFormat = new SimpleDateFormat("HH:mm");
        return timeFormat.format(calendar.getTime());
    }

    public static String searchWikipedia(String query) {
        // Implemente a lógica de pesquisa na Wikipedia aqui
        // Retorne os resultados encontrados
        return "Implementação da pesquisa na Wikipedia";
    }
}
